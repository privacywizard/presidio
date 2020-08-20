from presidio_analyzer import Pattern, PatternRecognizer


class EuropeIBANRecognizer(PatternRecognizer):
    """
    Recognizes ISO 13616 with ISO 3166 country code prefix in compact format using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: ISO 13616 with ISO 3166 country code prefix in compact format are a weak match, e.g., PL 10 1140 2017 0000 4202 0971 5311
    PATTERNS = [
        Pattern("IBAN (very weak)",
                r"[A-Z]{2}?[ ]?[0-9]{2}[ ]?[0-9]{4}[ ]?[0-9]{4}[ ]?[0-9]{4}[ ]?[0-9]{4}[ ]?[0-9]{4}[ ]?[0-9]{4}", 0.5),
    ]
    CONTEXT = ["ISO 13616 with ISO 3166 country code", "ISO 13616 with ISO 3166 country code prefix in compact format",
               "country code"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="EU_IBAN",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
