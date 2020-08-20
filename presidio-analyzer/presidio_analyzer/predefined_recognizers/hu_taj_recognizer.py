from presidio_analyzer import Pattern, PatternRecognizer


class HungaryTAJRecognizer(PatternRecognizer):
    """
    Recognizes Social insurance number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Social insurance number are a weak match, e.g., 123 456 789
    PATTERNS = [
        Pattern("TAJ (very weak)", r"[0-9]{3}[ ]?[0-9]{3}[ ][0-9]{3}", 0.5),
    ]
    CONTEXT = ["Social insurance number", "social insurance number", "TAJ szám"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="HU_TAJ",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
