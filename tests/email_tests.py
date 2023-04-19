"""
Copyright(C) Venidera Research & Development, Inc - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Marcos Leone Filho <marcos@venidera.com>
"""

import unittest
from email.mime.multipart import MIMEMultipart
from vmail import sender


class SendEmailTest(unittest.TestCase):
    """ Simple test to send an email """

    def test_method(self):
        """ Sends basic email as plain text """
        self.assertIsInstance(
            sender.send_email(toaddr='marcos@venidera.com',
                              fromaddr='suporte@venidera.com',
                              subject='UnitTest',
                              message='UnitTest Message Body'),
            MIMEMultipart)
