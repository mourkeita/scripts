#! /usr/bin/python
# coding: utf8


"""
This class deals with ISSUER or SUBJECT field on a
 a CSR or certificate and store them in a dictionnary.
- C : Country
- L : Locality
- O : Organization
- OU : Organization Unit
- CN : Common Name
- emailAddress : Email Address
"""

import global_ref
import M2Crypto
import re

from global_ref import *
from M2Crypto import X509


__author__ = "Mour KEITA"
__year__ = "2017"


def showme(message):
    """
    Prints a message given in parameters
    :param message (string):
    :return: None
    """
    print(message)


class CertificateFields:
    """
    Translates a data structure to store Certificate issuer
    or subject informations
    """
    def __init__(self, issuer):
        """
        Constructor of the CertificateFields class.
        Parses the issuer fields to extract informations

        :param issuer(string): string containing issuer
        or subject informations
        """
        self.reference = {
            REF_COUNTRY: {
                NAME: COUNTRY,
                REF_VALUE: '',
            },
            REF_COMMON_NAME: {
                REF_NAME: COMMON_NAME,
                REF_VALUE: ''
            },
            REF_LOCALITY: {
                REF_NAME: LOCALITY,
                REF_VALUE: ''
            },
            REF_STATE_LOCALITY: {
                REF_NAME: STATE_LOCALITY,
                REF_VALUE: ''
            },
            REF_ORGANIZATION: {
                REF_NAME: ORGANIZATION,
                REF_VALUE: ''
            },
            REF_ORGANIZATION_UNIT: {
                REF_NAME: ORGANIZATION_UNIT,
                REF_VALUE: ''
            },
            'emailAddress': {
                REF_NAME: 'Email',
                REF_VALUE: ''
            }
        }

        issuer_as_text = issuer.__str__()
        issuer_as_text = issuer_as_text.replace('/', '*')
        issuer_as_text = issuer_as_text.split('*')
        issuer_as_text.pop(0)

        i = 0
        for data in issuer_as_text:
            master_key = data.split('=')[0]
            secondary_key = REF_NAME
            secondary_value = data.split('=')[1]
            self.reference[master_key][REF_VALUE] = secondary_value
            i += 1

    def get_country(self):
        """
        Returns string containing the country of the issuer or subject
        :return: string
        """
        return self.reference[REF_COUNTRY][REF_VALUE]

    def get_locality(self):
        """
        Returns string containing the locality of the issuer or subject
        :return: string
        """
        return self.reference[REF_LOCALITY][REF_VALUE]

    def get_state_locality(self):
        """
        Returns string containing the state locality of the issuer or subject
        :return: string
        """
        return self.reference[REF_STATE_LOCALITY][REF_VALUE]

    def get_common_name(self):
        """
        Returns string containing the common name of the issuer or subject
        :return: string
        """
        return self.reference['CN'][REF_VALUE]

    def get_organization(self):
        """
        Returns string containing the organization of the issuer or subject
        :return: string
        """
        return self.reference[REF_ORGANIZATION][REF_VALUE]

    def get_organization_unit(self):
        """
        Returns string containing the organization unit of
        the issuer or subject
        :return: string
        """
        return self.reference[REF_ORGANIZATION_UNIT][REF_VALUE]

    def get_email(self):
        """
        Returns string containing the email of the issuer or subject
        :return: string
        """
        return self.reference['emailAddress'][REF_VALUE]
