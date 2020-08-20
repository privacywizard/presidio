from presidio_analyzer import Pattern, PatternRecognizer


class RomaniaCNFRecognizer(PatternRecognizer):
    """
    Recognizes Nr personal using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Nr personal are a weak match, e.g., 2121212121218
    PATTERNS = [
        Pattern("CNF (very weak)", r"[1-8][0-9]{2}[0,1][0-9][0-9]{2}[0-9]{6}", 0.5),
    ]
    CONTEXT = ["Nr personal", "nr personal"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="RO_CNF",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
