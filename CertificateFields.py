#! /usr/bin/python
# coding:utf8


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

import M2Crypto
import re
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
            'C': {
                'name': 'Country',
                'value': '',
            },
            'CN': {
                'name': 'Common Name',
                'value': ''
            },
            'L': {
                'name': 'Locality',
                'value': ''
            },
            'ST': {
                'name': 'State Locality',
                'value': ''
            },
            'O': {
                'name': 'Organization',
                'value': ''
            },
            'OU': {
                'name': 'Organization Unit',
                'value': ''
            },
            'emailAddress': {
                'name': 'Email',
                'value': ''
            }
        }

        issuer_as_text = issuer.__str__()
        issuer_as_text = issuer_as_text.replace('/', '*')
        issuer_as_text = issuer_as_text.split('*')
        issuer_as_text.pop(0)

        i = 0
        for data in issuer_as_text:
            master_key = data.split('=')[0]
            secondary_key = 'name'
            secondary_value = data.split('=')[1]
            self.reference[master_key]['value'] = secondary_value
            i += 1

    def get_country(self):
        """
        Returns string containing the country of the issuer or subject
        :return: string
        """
        return self.reference['C']['value']

    def get_locality(self):
        """
        Returns string containing the locality of the issuer or subject
        :return: string
        """
        return self.reference['L']['value']

    def get_state_locality(self):
        """
        Returns string containing the state locality of the issuer or subject
        :return: string
        """
        return self.reference['ST']['value']

    def get_common_name(self):
        """
        Returns string containing the common name of the issuer or subject
        :return: string
        """
        return self.reference['CN']['value']

    def get_organization(self):
        """
        Returns string containing the organization of the issuer or subject
        :return: string
        """
        return self.reference['O']['value']

    def get_organization_unit(self):
        """
        Returns string containing the organization unit of
        the issuer or subject
        :return: string
        """
        return self.reference['OU']['value']

    def get_email(self):
        """
        Returns string containing the email of the issuer or subject
        :return: string
        """
        return self.reference['emailAddress']['value']
