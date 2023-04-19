"""
Copyright(C) Venidera Research & Development, Inc - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Venidera Development Team <suporte@venidera.com>
"""

import os
import atexit
import shutil
import logging
import tempfile
import subprocess
import distutils.cmd
import distutils.log

from setuptools import find_packages, setup
from setuptools.command.install import install


__name__ = 'vmail'
__version__ = '0.0.2'
__author__ = 'Marcos Leone Filho'
__author_email__ = 'marcos@venidera.com'
__url__ = 'https://github.com/venidera/vmail.git'
__description__ = 'Utility for sending emails for Venidera (e.g. AWS).'
__keywords__ = 'venidera email'
__classifiers__ = [
    'Development Status :: 5 - Production/Stable',
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "Operating System :: Unix",
    "Topic :: Utilities"
]
__license__ = 'Proprietary'
__public_dependencies__ = []
__private_dependencies__ = []


class PostInstallCommand(install):
    """ customizing post-install actions """
    def __init__(self, *args, **kwargs):
        super(PostInstallCommand, self).__init__(*args, **kwargs)
        atexit.register(PostInstallCommand._post_install)

    @staticmethod
    def _post_install():
        # Manually installing dependencies
        for dep in __private_dependencies__:
            if 'github.com' in dep:
                token = os.environ.get(
                    'ACCESS_TOKEN', os.environ.get('GITHUB_ACCESS_TOKEN'))
                GITHUB_BRANCH = os.environ.get(
                    'GITHUB_BRANCH', 'master')
                # Creating prefix dependency urls
                if '{GITHUB_BRANCH}' in dep:
                    dep = dep.replace('{GITHUB_BRANCH}', GITHUB_BRANCH)
                prefix = f"git+https://{token}@{dep}" if token else f"git+ssh://git@{dep}"
                # Installing dependency
                os.system(f"pip install --upgrade {prefix}")
            elif 'bitbucket.org' in dep:
                # Capturing access token
                BITBUCKET_CREDENTIALS = os.environ.get('BITBUCKET_CREDENTIALS', None)
                token = "$(curl --data \"grant_type=client_credentials\" " + \
                    f"https://{BITBUCKET_CREDENTIALS}@bitbucket.org/site/oauth2/access_token " + \
                        "| grep 'access_token' | awk '{print $5}' | cut -c 2-85)" \
                    if BITBUCKET_CREDENTIALS else None
                # Creating prefix dependency urls
                prefix = f"git+https://x-token-auth:{token}@bitbucket.org/venidera" \
                    if token else 'git+ssh://git@bitbucket.org/venidera'
                os.system(f"pip install --upgrade {prefix}/{dep}.git")

        for dep in __public_dependencies__:
            if any([i + '://' in dep for i in ['ssh', 'http', 'https']]):
                os.system('pip install --upgrade %s' % dep)
        # Removing cache and egg files
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')
        os.system('find ' + __name__ + ' | grep -E ' +
                  '"(__pycache__|\\.pyc|\\.pyo$)" | xargs rm -rf')


class PylintCommand(distutils.cmd.Command):
    """ customizing pylint checks """
    user_options = [('pylint-rcfile=', None, 'path to Pylint config file')]

    def initialize_options(self):
        """ Pre-process options. """
        import requests
        # Capturing pylint file
        r = requests.get("https://venidera.sharepoint.com/:u:/s/venidera/" + \
            "EUL0UfQZw3lMjyaRB3fwsMkBImThS6U0UYOUYFTBawOAow?e=RY2fBx&download=1&isSPOFile=1")
        # Creating temporary repository
        repo = tempfile.mkdtemp()
        # Creating pylint file repository
        pylint = '%s/pylint.rc' % repo
        # Writing pylint file to temporary repository
        with open(pylint, 'wb') as w:
            w.write(r.content)
        # Adding custom pylint file
        self.pylint_rcfile = pylint if os.path.isfile(pylint) else ''

    def finalize_options(self):
        """ Post-process options. """
        if self.pylint_rcfile:
            assert os.path.exists(self.pylint_rcfile), (
                'Pylint config file %s does not exist.' % self.pylint_rcfile)

    def run(self):
        # Executing custom pylint
        c = subprocess.call('python setup.py lint --lint-rcfile %s' % (
            self.pylint_rcfile), shell=True)
        # Checking if call was executed with no errors
        if c != 0:
            logging.critical('Por favor, cheque seu código, pois há ' +
                             'problemas de escrita de código no padrão PEP8!')
        else:
            logging.info('Parabéns! Não foram detectados problemas ' +
                         'com a escrita do seu código.')
        # Removing the temporary directory
        shutil.rmtree('/'.join(self.pylint_rcfile.split('/')[:-1]))


# Running setup
setup(
    name=__name__,
    version=__version__,
    url=__url__,
    description=__description__,
    long_description=open('README.md').read(),
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    keywords=__keywords__,
    packages=find_packages(),
    install_requires=[
        'pylint',
        'requests',
        'setuptools-lint'
    ] + [p for p in __public_dependencies__ if not any(
        [i + '://' in p for i in ['ssh', 'http', 'https']])],
    classifiers=__classifiers__,
    cmdclass={
        'pylint': PylintCommand,
        'install': PostInstallCommand
    },
    test_suite="tests"
)
