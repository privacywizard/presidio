from presidio_analyzer import Pattern, PatternRecognizer


class FinlandHETURecognizer(PatternRecognizer):
    """
    Recognizes Personal identity code using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Personal identity code are a weak match, e.g., 101052-719E
    PATTERNS = [
        Pattern("HETU (very weak)", r"[0-9]{2}\.?[0,1][0-9]\.?[0-9]{2}[-+A][0-9]{3}[A-Z]", 0.5),
    ]
    CONTEXT = ["Personal identity code", "henkilötunnus", "personal identity code"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="FI_HETU",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
