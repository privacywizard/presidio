from presidio_analyzer import Pattern, PatternRecognizer


class GermanyPKRecognizer(PatternRecognizer):
    """
    Recognizes Personenkennziffer using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Personenkennziffer are a weak match, e.g., 261083-C-20917
    PATTERNS = [
        Pattern("PK (very weak)", r"[0-9]{2}[0,1][0-9][0-9]{2}-[A-Z]-[0-9]{5}", 0.5),
    ]
    CONTEXT = ["Personenkennziffer", "personenkennziffer", "Bundeswehr"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="DE_PK",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
