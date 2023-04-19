"""
Copyright(C) Venidera Research & Development, Inc - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Marcos Leone Filho <marcos@venidera.com>
"""

import logging
from vmail import sender

# General procedures to show the log
logging.basicConfig(
    format='%(asctime)s - %(levelname)s: ' +
    '(%(filename)s:%(funcName)s at %(lineno)d): %(message)s',
    datefmt='%b %d %H:%M:%S',
    level=logging.INFO)

# Creating argument parser object
sender.send_email(toaddr='marcos@venidera.com',
                  fromaddr='suporte@venidera.com',
                  subject='Teste 1 2 3',
                  message='mensagem de teste 1 2 3',
                  attach_files=['./scripts/run.py'])
