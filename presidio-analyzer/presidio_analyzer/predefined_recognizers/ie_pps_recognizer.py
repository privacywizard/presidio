from presidio_analyzer import Pattern, PatternRecognizer


class IrelandPPSRecognizer(PatternRecognizer):
    """
    Recognizes Personal Public Service Number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Personal Public Service Number are a weak match, e.g., 1234567A 1234567FW
    PATTERNS = [
        Pattern("PPS (very weak)", r"[0-9]{7}[A-Z]W?", 0.5),
    ]
    CONTEXT = ["Personal Public Service Number", "personal public service number"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="IE_PPS",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
