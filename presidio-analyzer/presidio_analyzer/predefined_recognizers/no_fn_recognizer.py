from presidio_analyzer import Pattern, PatternRecognizer


class NorwayFNRecognizer(PatternRecognizer):
    """
    Recognizes Fødselsnummer using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Fødselsnummer are a weak match, e.g., 010168 46647
    PATTERNS = [
        Pattern("FN (very weak)", r"[0-9]{2}[0,1][0-9][0-9]{2}[ ]?[0-9]{5}", 0.5),
    ]
    CONTEXT = ["Fødselsnummer", "fødselsnummer"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="NO_FN",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
