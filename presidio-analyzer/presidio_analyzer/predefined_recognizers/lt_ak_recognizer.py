from presidio_analyzer import Pattern, PatternRecognizer


class LithuaniaAKRecognizer(PatternRecognizer):
    """
    Recognizes Personal code using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Personal code are a weak match, e.g., 45911231023
    PATTERNS = [
        Pattern("AK (very weak)", r"[3-6][0-9]{2}[0,1][0-9][0-9]{2}[0-9]{4}", 0.5),
    ]
    CONTEXT = ["Personal code", "personal code", "Asmens kodas"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="LT_AK",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
