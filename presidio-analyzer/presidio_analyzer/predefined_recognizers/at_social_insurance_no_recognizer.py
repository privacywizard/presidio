from presidio_analyzer import Pattern, PatternRecognizer


class AustriaSIMRecognizer(PatternRecognizer):
    """
    Recognizes Austria Social Insurance number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Social insurance number are a weak match, e.g., 1234030869
    PATTERNS = [
        Pattern("ASVG (very weak)", r"[0-9]{10}", 0.5),
    ]
    CONTEXT = ["Social insurance number", "social insurance number", "social insurance",]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="ASVG",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
