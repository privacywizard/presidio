from presidio_analyzer import Pattern, PatternRecognizer


class GreeceTautotitaRecognizer(PatternRecognizer):
    """
    Recognizes Tautotita using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Tautotita are a weak match, e.g., P 000007
    PATTERNS = [
        Pattern("Tautotita (very weak)", r"[A-Z][ -]?[0-9]{6}", 0.5),
    ]
    CONTEXT = ["Tautotita", "tautotita"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="GR_Tautotita",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
