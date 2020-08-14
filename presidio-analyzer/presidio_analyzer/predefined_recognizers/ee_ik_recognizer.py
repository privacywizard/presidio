from presidio_analyzer import Pattern, PatternRecognizer


class EstoniaIsikukoodRecognizer(PatternRecognizer):
    """
    Recognizes Estonia Isikukood using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: new national identification number are a weak match, e.g., 1234030869
    PATTERNS = [
        Pattern("IK (very weak)", r"[1-6][0-9]{2}[1,2][0-9][0-9]{2}[0-9]{4}", 0.5),
    ]
    CONTEXT = ["Estonia Isikukood",]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="EE_IK",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
