from presidio_analyzer import Pattern, PatternRecognizer


class SwitzerlandAVSRecognizer(PatternRecognizer):
    """
    Recognizes Old AVS format with personal data encoded using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Old AVS format with personal data encoded are a weak match, e.g., 324.65.242.000
    PATTERNS = [
        Pattern("AVS (very weak)", r"[0-9]{3}\.?[0-9]{2}\.?[0-9]{3}\.?[0-9]{3}", 0.5),
    ]
    CONTEXT = ["Old AVS format with personal data encoded", "old avs format with personal data encoded"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="CH_AVS",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
