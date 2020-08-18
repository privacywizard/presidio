from .aba_routing_recognizer import AbaRoutingRecognizer
from .at_sspin_recognizer import AustriaSSPINRecognizer
from .at_zmr_zahl_recognizer import AustriaNIMRecognizer
from .at_social_insurance_no_recognizer import AustriaSIMRecognizer
from .be_national_id_recognizer import BelgiumNationalIDRecognizer
from .be_beid_recognizer import BelgiumBEIDRecognizer
from .bg_civil_number_recognizer import BulgariaUniformCivilNumberRecognizer
from .bg_egn_recognizer import BulgariaEGNRecognizer
from .credit_card_recognizer import CreditCardRecognizer
from .cz_rc_recognizer import CzechSlovakiaRCRecognizer
from .dk_cpr_number_recognizer import DenmarkCPRNumberRecognizer
from .ee_ik_recognizer import EstoniaIsikukoodRecognizer
from .imei_recognizer import IMEIRecognizer
from .crypto_recognizer import CryptoRecognizer
from .domain_recognizer import DomainRecognizer
from .email_recognizer import EmailRecognizer
from .iban_recognizer import IbanRecognizer
from .in_aadhar_card_recognizer import AadharRecognizer
from .ip_recognizer import IpRecognizer
from .sg_fin_recognizer import SgFinRecognizer
from .spacy_recognizer import SpacyRecognizer
from .stanza_recognizer import StanzaRecognizer
from .uk_nhs_recognizer import NhsRecognizer
from .us_bank_recognizer import UsBankRecognizer
from .us_driver_license_recognizer import UsLicenseRecognizer
from .us_itin_recognizer import UsItinRecognizer
from .us_passport_recognizer import UsPassportRecognizer
from .us_phone_recognizer import UsPhoneRecognizer
from .us_ssn_recognizer import UsSsnRecognizer

NLP_RECOGNIZERS = {"spacy": SpacyRecognizer, "stanza": StanzaRecognizer}

__all__ = [
    "AadharRecognizer",
    "AbaRoutingRecognizer",
    "AustriaNIMRecognizer",
    "AustriaSIMRecognizer",
    "AustriaSSPINRecognizer",
    "BelgiumNationalIDRecognizer",
    "BulgariaUniformCivilNumberRecognizer",
    "BulgariaEGNRecognizer",
    "BelgiumBEIDRecognizer",
    "CreditCardRecognizer",
    "CryptoRecognizer",
    "CzechSlovakiaRCRecognizer",
    "DenmarkCPRNumberRecognizer",
    "DomainRecognizer",
    "EmailRecognizer",
    "EstoniaIsikukoodRecognizer",
    "IbanRecognizer",
    "IMEIRecognizer",
    "IpRecognizer",
    "NhsRecognizer",
    "SgFinRecognizer",
    "SpacyRecognizer",
    "StanzaRecognizer",
    "UsBankRecognizer",
    "UsItinRecognizer",
    "UsLicenseRecognizer",
    "UsPassportRecognizer",
    "UsPhoneRecognizer",
    "UsSsnRecognizer",
    "NLP_RECOGNIZERS",
]
