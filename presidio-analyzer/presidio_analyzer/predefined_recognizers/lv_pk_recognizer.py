from presidio_analyzer import Pattern, PatternRecognizer


class LatviaPKRecognizer(PatternRecognizer):
    """
    Recognizes Personal no using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Personal no are a weak match, e.g., 161171-22345
    PATTERNS = [
        Pattern("PK (very weak)", r"[0-9]{3}[0,1][0-9][0-9]-[0-9]{5}", 0.5),
    ]
    CONTEXT = ["Personal no", "personal no", "Personas kodas"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="LV_PK",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
