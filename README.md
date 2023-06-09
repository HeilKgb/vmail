

# Utility for sending emails within Venidera

![GitHub Release](https://img.shields.io/badge/release-v0.0.2-blue.svg)
![GitHub license](https://img.shields.io/badge/license-Proprietary-yellow.svg)

This tutorial walks you through how to send emails within Venidera.

## Table of contents
[TOC]

## Requirements

* Python 3.6 or superior (`sudo apt-get install python3.6` under Linux)
* Python virtual environment (`sudo apt-get install python3.6-venv` under Linux)

## Package structure

The initial directory structure should look like this:

- `vmail` The top-level package directory.
    -   `README.md`  Description of the package -- should be written in Markdown.
    -   `setup.py` The script for building/installing the package.
    -   `LICENSE` Text of the license you choose.
    -   `.gitignore` Specifies untracked files that Git should ignore.
    -   `vmail` Base package module.
        -   `sender.py`  Routines for sending an email.
    -   `lib` Auxiliary package routines.
        -   `config.py`  Stores configuration for available Venidera SMTP services.
    -   `scripts` Directory with top-level user scripts.
        -   `run.py` A standard script for running the application.
    -   `tests` Collection of general-purpose tests.
        -   `email_tests.py` Test scripts for module `sender.py`.

## Development and Tests

### 1. Cloning the repository
The first step aims to clone the `vmail` repository from Github. If you don't have SSH configured, then you need to use the HTTPS protocol to communicate between your local system and Github Cloud. It is possible to change the current working directory to the location where you want the cloned directory to be made.
```bash
$ mkdir ~/git
$ git clone git@github.com:venidera/vmail.git ~/git/vmail
$ cd ~/git/vmail
```

### 2. Installing the package
 Start by creating a new virtual environment for your project. Next, update the packages `pip` and `setuptools` to the latest version. Then install the package itself.
```bash
$ /usr/bin/python3.6 -m venv --prompt="project" venv
$ source venv/bin/activate
(project) $ pip install --upgrade setuptools pip
(project) $ python setup.py install
```

### 3. Code checking
It is also possible to check for errors in Python code using:
```bash
(project) $ python setup.py pylint
```
Pylint is a tool that tries to enforce a coding standard and looks for  [code smells](https://martinfowler.com/bliki/CodeSmell.html). Pylint will display several messages as it analyzes the code and it can also be used for displaying some statistics about the number of warnings and errors found in different files. The current package uses a custom [configuration file](https://drive.google.com/a/venidera.com/uc?id=1SeUYS-g-MTj-7a_XYwaXZUQpDiQ26JuW), tailored to Venidera code standard.


### 4. Testing package modules
Python tests are Python classes that reside in separate files from the code being tested. In this project, module tests are based on Python `unittest` package and are located in the `tests` directory. They can be run by the following code: 
```bash
(project) $ python setup.py test
```
In general, the developer can create and perform as many tests as he needs. However, it is important to validate them before committing a new change to the Bitbucket Cloud, as a way of avoiding errors. It is also important to mention that tests will only be performed if test classes extend the `unittest.TestCase` object.


### 5. Running the application
To run your package (and also to generate a script that helps other developers to execute your package), put your package's execution routines into `scripts/run.py` directory. Then, once package syntax is following Venidera code standards and all tests were performed, you can run the application by executing the following code:
```bash
(project) $ python scripts/run.py
```

## Troubleshooting

Please file a Github issue to [report a bug](https://github.org/venidera/data-models/issues?status=new&status=open).

## Maintainers

-   Marcos Leone Filho - [marcos@venidera.com](mailto:marcos@venidera.com)
-   Venidera Development Team -  [suporte@venidera.com](mailto:suporte@venidera.com)

## License

This package is released and distributed under the license  [GNU GPL Version 3, 29 June 2007](https://www.gnu.org/licenses/gpl-3.0.html).#   v m a i l  
 