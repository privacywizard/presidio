from presidio_analyzer import Pattern, PatternRecognizer


class CzechSlovakiaRCRecognizer(PatternRecognizer):
    """
    Recognizes Birth Number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Birth Number are a weak match, e.g., 685229/4449
    PATTERNS = [
        Pattern("RC (very weak)", r"[0-9]{2}[0,1,5][0-9][0-9]{2}\/?[0-9]{4}", 0.5),
    ]
    CONTEXT = ["Birth Number", "Rodné číslo", "birth number"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="CZ_RC",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
