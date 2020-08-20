from presidio_analyzer import Pattern, PatternRecognizer


class NetherlandsBSNRecognizer(PatternRecognizer):
    """
    Recognizes Citizen's Service Number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Citizen's Service Number are a weak match, e.g., 987654321
    PATTERNS = [
        Pattern("BSN (very weak)", r"[0-9]{9}", 0.5),
    ]
    CONTEXT = ["Citizen's Service Number", "citizen's service number", "Burgerservicenummer", "sofinummer"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="NL_BSN",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
