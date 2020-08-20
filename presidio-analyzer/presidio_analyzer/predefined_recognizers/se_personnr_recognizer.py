from presidio_analyzer import Pattern, PatternRecognizer


class SwedenPersonnrRecognizer(PatternRecognizer):
    """
    Recognizes Personal id number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Personal id number are a weak match, e.g., 610321-3499
    PATTERNS = [
        Pattern("Personnr (very weak)", r"[0-9]{2}[0-1][0-9][0-9]{2}[-+][0-9]{4}", 0.5),
    ]
    CONTEXT = ["Personal id number", "personal id number"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="SE_Personnr",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
