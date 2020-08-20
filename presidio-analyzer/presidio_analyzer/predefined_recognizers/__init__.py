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
#from .dk_cpr_number_recognizer import DenmarkCPRNumberRecognizer
from .de_pk_recognizer import GermanyPKRecognizer
from .de_steuer_id_recognizer import GermanySteuerIDRecognizer
from .de_vsnr_rvnr_recognizer import GermanyVSNRRVNRRecognizer
from .ee_ik_recognizer import EstoniaIsikukoodRecognizer
from .eu_iban_recognizer import EuropeIBANRecognizer
from .es_dni_recognizer import SpainDNIRecognizer
from .fi_hetu_recognizer import FinlandHETURecognizer
from .fr_nir_recognizer import FranceNIRRecognizer
from .gr_tautotita_recognizer import GreeceTautotitaRecognizer
from .imei_recognizer import IMEIRecognizer
from .ie_pps_recognizer import IrelandPPSRecognizer
from .it_cf_recognizer import ItalyCFRecognizer
from .lv_pk_recognizer import LatviaPKRecognizer
from .lt_ak_recognizer import LithuaniaAKRecognizer
from .nl_bsn_recognizer import NetherlandsBSNRecognizer
from .no_fn_recognizer import NorwayFNRecognizer
from .crypto_recognizer import CryptoRecognizer
from .domain_recognizer import DomainRecognizer
from .dk_cpr_recognizer import DenmarkCPRRecognizer
from .email_recognizer import EmailRecognizer
from .hu_szam_recognizer import HungarySzamRecognizer
from .hu_taj_recognizer import HungaryTAJRecognizer
from .iban_recognizer import IbanRecognizer
from .in_aadhar_card_recognizer import AadharRecognizer
from .ip_recognizer import IpRecognizer
from .ro_cnf_recognizer import RomaniaCNFRecognizer
from .sg_fin_recognizer import SgFinRecognizer
from .spacy_recognizer import SpacyRecognizer
from .stanza_recognizer import StanzaRecognizer
from .se_personnr_recognizer import SwedenPersonnrRecognizer
from .ch_avs_2008_recognizer import SwitzerlandAVS2008Recognizer
from .ch_avs_recognizer import SwitzerlandAVSRecognizer
from .pl_pesel_recognizer import PolandPESELRecognizer
from .uk_nhs_recognizer import NhsRecognizer
from .us_bank_recognizer import UsBankRecognizer
from .us_driver_license_recognizer import UsLicenseRecognizer
from .us_itin_recognizer import UsItinRecognizer
from .us_passport_recognizer import UsPassportRecognizer
from .us_phone_recognizer import UsPhoneRecognizer
from .us_ssn_recognizer import UsSsnRecognizer
from .uk_ni_recognizer import UKNIRecognizer
from .uk_nino_recognizer import UKNINORecognizer

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
    "DenmarkCPRRecognizer",
    "DomainRecognizer",
    "EmailRecognizer",
    "EstoniaIsikukoodRecognizer",
    "EuropeIBANRecognizer",
    "FinlandHETURecognizer",
    "FranceNIRRecognizer",
    "GermanyPKRecognizer",
    "GermanySteuerIDRecognizer",
    "GermanyVSNRRVNRRecognizer",
    "GreeceTautotitaRecognizer",
    "HungarySzamRecognizer",
    "HungaryTAJRecognizer",
    "IbanRecognizer",
    "IMEIRecognizer",
    "IpRecognizer",
    "IrelandPPSRecognizer",
    "ItalyCFRecognizer",
    "LatviaPKRecognizer",
    "LithuaniaAKRecognizer",
    "NetherlandsBSNRecognizer",
    "NorwayFNRecognizer",
    "NhsRecognizer",
    "RomaniaCNFRecognizer",
    "SgFinRecognizer",
    "SpacyRecognizer",
    "StanzaRecognizer",
    "SpainDNIRecognizer",
    "SwedenPersonnrRecognizer",
    "SwitzerlandAVS2008Recognizer",
    "SwitzerlandAVSRecognizer",
    "PolandPESELRecognizer",
    "UsBankRecognizer",
    "UsItinRecognizer",
    "UsLicenseRecognizer",
    "UsPassportRecognizer",
    "UsPhoneRecognizer",
    "UsSsnRecognizer",
    "UKNIRecognizer",
    "UKNINORecognizer",
    "NLP_RECOGNIZERS",
]
