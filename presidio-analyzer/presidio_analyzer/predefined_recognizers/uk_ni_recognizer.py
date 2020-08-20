from presidio_analyzer import Pattern, PatternRecognizer


class UKNIRecognizer(PatternRecognizer):
    """
    Recognizes National identification number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: National identification number are a weak match, e.g., JG103759A
    PATTERNS = [
        Pattern("NI (very weak)", r"[A-CEGHJ-PR-TW-Z][A-CEGHJ-NPR-TW-Z]{1}[0-9]{6}[A-DFM]?", 0.5),
    ]
    CONTEXT = ["National identification number", "national identification number"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="UK_NI",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
