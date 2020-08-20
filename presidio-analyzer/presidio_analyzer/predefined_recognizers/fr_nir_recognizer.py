from presidio_analyzer import Pattern, PatternRecognizer


class FranceNIRRecognizer(PatternRecognizer):
    """
    Recognizes Social security numberusing regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Social security number are a weak match, e.g., 1 51 02 46102 043 25
    PATTERNS = [
        Pattern("NIR (very weak)", r"[1,2][ ]?[0-9]{2}[ ]?[0,1,2,3,5][0-9][ ]?[0-9A-Z]{5}[ ]?[0-9]{3}[ ]?[0-9]{2}", 0.5),
    ]
    CONTEXT = ["Social security number", "social security number", "INSEE"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="FR_NIR",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
