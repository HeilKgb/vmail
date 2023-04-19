"""
Copyright(C) Venidera Research & Development, Inc - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Marcos Leone Filho <marcos@venidera.com>
"""


def get_config(config_name='aws'):
    """ Returns a given configuration set for smtp """
    smtp_configs = {
        "aws": {
            "smtp_server": "email-smtp.us-east-1.amazonaws.com",
            "smtp_username": "AKIATGDGNXMSLV6W5KEW",
            "smtp_password": "BLbz0ir66RwEY7VEmPoi8PNtnswGNPCmBMxng/Tx69AL",
            "smtp_port": "587"}}
    return smtp_configs[config_name]
