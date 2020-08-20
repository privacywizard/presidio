from presidio_analyzer import Pattern, PatternRecognizer


class HungarySzamRecognizer(PatternRecognizer):
    """
    Recognizes Personal identfication number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Personal identfication number are a weak match, e.g., 1 651105 6666
    PATTERNS = [
        Pattern("Szam (very weak)", r"[1-8][ ]?[0-9]{2}[0,1][0-9][0-9]{2}[ ]?[0-9]{4}", 0.5),
    ]
    CONTEXT = ["Personal identfication number", "Személyi szám", "personal identfication number"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="HU_Szam",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
