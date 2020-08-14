from presidio_analyzer import Pattern, PatternRecognizer


class AustriaSSPINRecognizer(PatternRecognizer):
    """
    Recognizes Austria new national identification number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: new national identification number are a weak match, e.g., 1234030869
    PATTERNS = [
        Pattern("ssPIN (very weak)", r"[A-Za-z0-9+/]{22}[A-Za-z0-9+/=][A-Za-z0-9+/=]", 0.5),
    ]
    CONTEXT = ["New national identification number", "new national identification number", "New National identification number",]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="ssPIN",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
