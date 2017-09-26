#! /usr/bin/python
# coding: utf8


"""
This code takes a CSR or X509 certificate and displays its attributes.
- ca
- issuer
- subject
- locality
- organization
- ou
- cn
- email
- begin date
- expiration date
TODO
This test even a certificate is revokated or good.

To run this code :
python CertificateTreatment.py --cert "certificate"
"""

import argparse
import CertificateFields
import M2Crypto
import re

from argparse import ArgumentParser
from global_ref import *
from CertificateFields import CertificateFields, showme
from M2Crypto import X509


__author__ = "Mour KEITA"
__year__ = "2017"


class CertificateTreatment:
    """
    This class makes different treatments on a certificate to display
    informations on Issuer, Subject, Public key...
    """
    def __init__(self, certificat):
        """
        Create a CertificateTreatment object to treat informations on
        the certificate given in parameters
        :param certificat: X509 object
        """
        self.cert = X509.load_cert(certificat)
        self.issuer = self.get_issuer()
        self.subject = self.get_subject()
        self.issuer_info = CertificateFields(self.issuer)
        self.subject_info = CertificateFields(self.subject)

    def get_cert(self):
        """
        Returns the certificate given on constructor
        :return: X509 object
        """
        return self.cert

    def show_version(self):
        """
        Prints certificate version
        :return: None
        """
        showme("%s %s" % (VERSION_MESSAGE, self.cert.get_version()))

    def show_extension(self):
        """
        Prints certificate extension
        :return: None
        """
        showme("%s %s" % (EXTENSION_coUNT_MESSAGE, self.cert.get_ext_count()))

    def show_fingerprint(self):
        """
        Prints certificates fingerprint
        :return: None
        """
        message_fingerprint = self.cert.get_fingerprint()
        showme("%s %s" % (FINGERPRINT_MESSAGE, message_fingerprint))

    def show_valid_not_before(self):
        """
        Prints not before validation date of a certificate
        :return: None
        """
        showme("%s %s" % (VALID_NOT_BEFORE_MESSAGE, self.cert.get_not_before()))

    def show_valid_not_after(self):
        """
        Prints expiration date of the certificate
        :return: None
        """
        showme("%s %s" % (VALID_NOT_AFTER_MESSAGE ,self.cert.get_not_after()))

    def show_serial_number(self):
        """
        Prints serial number of a certificate
        :return: None
        """
        showme("%s %s" % (SERIAL_NUMBER_MESSAGE, self.cert.get_serial_number()))

    def show_public_key(self):
        """
        Prints the certificate public key
        :return: None
        """
        public_key = self.cert.get_pubkey()
        #showme("Private key :\n%s" % public_key.as_pem())
        public_key_rsa = public_key.get_rsa()
        showme("%s %s" % (PUBLIC_KEY_MESSAGE, public_key_rsa.as_pem()))

    def set_issuer(self):
        """
        Set the issuer attribute from the certificate field: issuer
        :return: None
        """
        self.issuer = self.cert.get_issuer()

    def get_issuer(self):
        """
        Returns a string corresponding to the certificate issuer
        :return: string
        """
        issuer = self.cert.get_issuer()
        return issuer

    def show_issuer_as_text(self):
        """
        Prints certificate's issuer in raw data
        :return: None
        """
        showme(self.set_issuer)

    def get_issuer_locality(self):
        """
        Returns issuer locality
        :return: string
        """
        return self.issuer_info.get_locality()

    def show_issuer_locality(self):
        """
        Prints issuer locality
        :return: None
        """
        showme("%s %s : %s" % \
               (ISSUER, self.issuer_info.reference[REF_LOCALITY][REF_NAME]\
                .lower(), self.get_issuer_locality()))

    def get_issuer_country(self):
        """
        Returns issuer country
        :return: string
        """
        return self.issuer_info.get_country()

    def show_issuer_country(self):
        """
        Displays issuer country
        :return: None
        """
        showme("%s %s : %s" % \
               (ISSUER, self.issuer_info.reference[REF_COUNTRY][REF_NAME]\
                .lower(), self.get_issuer_country()))

    def get_issuer_state_locality(self):
        """
        Returns issuer state locality
        :return: string
        """
        return self.issuer_info.get_state_locality()

    def show_issuer_state_locality(self):
        """
        Displays issuer state locality
        :return: None
        """
        showme("%s %s : %s" % \
               (ISSUER, self.issuer_info.reference[REF_STATE_LOCALITY][REF_NAME]\
                .lower(), self.get_issuer_state_locality()))

    def get_issuer_common_name(self):
        """
        Returns issuer common name
        :return: string
        """
        return self.issuer_info.get_common_name()

    def show_issuer_common_name(self):
        """
        Displays issuer common name
        :return: None
        """
        showme("%s %s : %s" % \
               (ISSUER, self.issuer_info.reference[REF_COMMON_NAME][REF_NAME]\
                .lower(), self.get_issuer_common_name()))

    def get_issuer_organization(self):
        """
        Returns issuer organization
        :return: string
        """
        return self.issuer_info.get_organization()

    def show_issuer_organization(self):
        """
        Displays issuer organization
        :return: None
        """
        showme("%s %s : %s" % \
               (ISSUER, self.issuer_info.reference[REF_ORGANIZATION][REF_NAME]\
                .lower(), self.get_issuer_organization()))

    def get_issuer_organization_unit(self):
        """
        Returns issuer organization unit
        :return: string
        """
        return self.issuer_info.get_organization_unit()

    def show_issuer_organization_unit(self):
        """
        Displays issuer organization unit
        :return: None
        """
        showme("%s %s : %s" % \
               (ISSUER, self.issuer_info.reference[REF_ORGANIZATION_UNIT][REF_NAME]\
                .lower(), self.get_issuer_organization_unit()))

    def get_issuer_email(self):
        """
        Returns issuer email
        :return: string
        """
        return self.issuer_info.get_email()

    def show_issuer_email(self):
        """
        Displays issuer email
        :return: None
        """
        showme("%s %s : %s" % \
               (ISSUER, self.issuer_info.reference[REF_EMAIL_ADDRESS][REF_NAME]\
                .lower(), self.get_issuer_email()))

    def set_subject(self):
        """
        Assign to subject attribute value from the certificate subject
        :return: None
        """
        self.subject = self.cert.get_subject()

    def get_subject(self):
        """
        Returns subject's raw data from certificate
        :return: string
        """
        subject = self.cert.get_subject()
        return subject

    def show_subject_as_text(self):
        """
        Display subject as raw data
        :return: None
        """
        showme(self.get_subject())

    def show_subject(self):
        """
        Prints subject's raw data of a certificate X509
        :return: None
        """
        showme("%s %s" % (SUBJECT, self.cert.get_subject()))

    def get_subject_locality(self):
        """
        Returns subject's locality of a certificate X509
        :return: string
        """
        return self.subject_info.get_locality()

    def show_subject_locality(self):
        """
        Prints subject's locality of a certificate X509
        :return: None
        """
        showme("%s %s : %s" % \
               (SUBJECT, self.subject_info.reference[REF_LOCALITY][REF_NAME]\
                .lower(), self.get_subject_locality()))

    def get_subject_country(self):
        """
        Returns subject's country of a certificate X509
        :return: string
        """
        return self.subject_info.get_country()

    def show_subject_country(self):
        """
        Prints subject's country of a certificate X509
        :return: None
        """
        showme("%s %s : %s" % \
               (SUBJECT, self.subject_info.reference[REF_COUNTRY][REF_NAME]\
                .lower(), self.get_subject_country()))

    def get_subject_state_locality(self):
        """
        Returns subject's state locality of a certificate X509
        :return: string
        """
        return self.subject_info.get_state_locality()

    def show_subject_state_locality(self):
        """
        Prints subject's state locality of a certificate X509
        :return: None
        """
        showme("%s %s : %s" % \
               (SUBJECT, self.subject_info.reference[REF_STATE_LOCALITY][REF_NAME]\
                .lower(), self.get_subject_state_locality()))

    def get_subject_common_name(self):
        """
        Returns subject's common name of a certificate X509
        :return: string
        """
        return self.subject_info.get_common_name()

    def show_subject_common_name(self):
        """
        Prints subject's common name of a certificate X509
        :return: None
        """
        showme("%s %s : %s" % \
               (SUBJECT, self.subject_info.reference[REF_COMMON_NAME][REF_NAME]\
                .lower(), self.get_subject_common_name()))

    def get_subject_organization(self):
        """
        Returns subject's organization of a certificate X509
        :return: string
        """
        return self.subject_info.get_organization()

    def show_subject_organization(self):
        """
        Prints subject's organization of a certificate X509
        :return: None
        """
        showme("%s %s : %s" % \
               (SUBJECT, self.subject_info.reference[REF_ORGANIZATION][REF_NAME]\
                .lower(), self.get_subject_organization()))

    def get_subject_organization_unit(self):
        """
        Returns subject's organization unit of a certificate X509
        :return: string
        """
        return self.subject_info.get_organization_unit()

    def show_subject_organization_unit(self):
        """
        Prints subject's organization of a certificate X509
        :return: None
        """
        showme("%s %s : %s" % \
               (SUBJECT, self.subject_info.reference[REF_ORGANIZATION_UNIT][REF_NAME]\
                .lower(), self.get_subject_organization_unit()))

    def get_subject_email(self):
        """
        Returns subject's email of a certificate X509
        :return: string
        """
        return self.subject_info.get_email()

    def show_subject_email(self):
        """
        Prints subject's email of a certificate X509
        :return: None
        """
        showme("%s %s : %s" % \
               (SUBJECT, self.subject_info.reference[REF_EMAIL_ADDRESS][REF_NAME]\
                .lower(), self.get_subject_email()))

    def show_all(self):
        """
        Prints all informations of a certificate X509
        :return: None
        """
        showme("Begin")
        self.show_serial_number()
        self.show_fingerprint()
        self.show_version()
        self.show_valid_not_before()
        self.show_valid_not_after()
        self.show_public_key()
        self.show_issuer_country()
        self.show_issuer_state_locality()
        self.show_issuer_locality()
        self.show_issuer_organization()
        self.show_issuer_organization_unit()
        self.show_issuer_common_name()
        self.show_issuer_email()
        self.show_subject_country()
        self.show_subject_state_locality()
        self.show_subject_locality()
        self.show_subject_organization()
        self.show_subject_organization_unit()
        self.show_subject_common_name()
        self.show_subject_email()
        showme("End.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Give a certificate in \
    arguments please !")
    parser.add_argument("--cert", dest="cert", action="store",\
                        help='Give a certificate name')
    args = parser.parse_args()
    my_certificate = CertificateTreatment(args.cert)
    my_certificate.show_all()
