from presidio_analyzer import Pattern, PatternRecognizer


class GermanyVSNRRVNRRecognizer(PatternRecognizer):
    """
    Recognizes Versicherungsnummer, Rentenversicherungsnummer using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Versicherungsnummer, Rentenversicherungsnummer are a weak match, e.g., 65170839J003
    PATTERNS = [
        Pattern("VSNR_RVNR (very weak)", r"[0-9]{2}[0-9]{2}[0,1][0-9][0-9]{2}[A-Z][0-9]{2}[0-9]", 0.5),
    ]
    CONTEXT = ["Versicherungsnummer", "Rentenversicherungsnummer", "versicherungsnummer, rentenversicherungsnummer"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="DE_VSNR_RVNR",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
