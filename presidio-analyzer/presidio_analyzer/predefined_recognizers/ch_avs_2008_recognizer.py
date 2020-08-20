from presidio_analyzer import Pattern, PatternRecognizer


class SwitzerlandAVS2008Recognizer(PatternRecognizer):
    """
    Recognizes New AVS format using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: New AVS format are a weak match, e.g., 756.5152.7017.84
    PATTERNS = [
        Pattern("AVS_2008 (very weak)", r"756\.?[0-9]{4}\.?[0-9]{4}\.?[0-9]{2}", 0.5),
    ]
    CONTEXT = ["New AVS format", "16 digits with constant prefix 756, which is ISO 3166-1 country code"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="CH_AVS_2008",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
