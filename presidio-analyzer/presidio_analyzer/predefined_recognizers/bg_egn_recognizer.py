from presidio_analyzer import Pattern, PatternRecognizer


class BulgariaEGNRecognizer(PatternRecognizer):
    """
    Recognizes Uniform Civil Number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Uniform Civil Number are a weak match, e.g., 7608010133
    PATTERNS = [
        Pattern("EGN (very weak)", r"[0-9]{2}[0,1,2,4][0-9][0-9]{2}[0-9]{4}", 0.5),
    ]
    CONTEXT = ["Uniform Civil Number", "Единен граждански номер", "uniform civil number"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="BG_EGN",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
