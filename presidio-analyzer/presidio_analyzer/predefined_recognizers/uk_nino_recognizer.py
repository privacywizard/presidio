from presidio_analyzer import Pattern, PatternRecognizer


class UKNINORecognizer(PatternRecognizer):
    """
    Recognizes National insurance number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: National insurance number are a weak match, e.g., JG 12 13 16 A, AB123456C
    PATTERNS = [
        Pattern("NINO (very weak)",
                r"[A-Z]{2}?[ ]?[0-9]{2}[ ]?[0-9]{2}[ ]?[0-9]{2}[ ]?[ ]?[A-Z],?[ ]?[A-CEGHJ-PR-TW-Z][A-CEGHJ-NPR-TW-Z]{1}[0-9]{6}[A-DFM]?",
                0.5),
    ]
    CONTEXT = ["National insurance number", "national insurance number"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="UK_NINO",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
