from presidio_analyzer import Pattern, PatternRecognizer


class PolandPESELRecognizer(PatternRecognizer):
    """
    Recognizes National identification number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: National identification number are a weak match, e.g., 44051401458
    PATTERNS = [
        Pattern("PESEL (very weak)", r"[0-9]{4}[0-3]{1}[0-9}{1}[0-9]{6}", 0.5),
    ]
    CONTEXT = ["National identification number", "national identification number"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="PL_PESEL",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
