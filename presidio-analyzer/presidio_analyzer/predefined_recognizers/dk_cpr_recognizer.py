from presidio_analyzer import Pattern, PatternRecognizer


class DenmarkCPRRecognizer(PatternRecognizer):
    """
    Recognizes CPR-number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: CPR-nummer are a weak match, e.g., 020955-2017
    PATTERNS = [
        Pattern("CPR (very weak)", r"[0-9]{2}[0,1][0-9][0-9]{2}-[0-9]{4}", 0.5),
    ]
    CONTEXT = ["CPR-nummer", "personnummer", "cpr-nummer"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="DK_CPR",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
