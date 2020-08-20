from presidio_analyzer import Pattern, PatternRecognizer


class ItalyCFRecognizer(PatternRecognizer):
    """
    Recognizes Codice fiscale	 using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Codice fiscale are a weak match, e.g., PLDTLL47S04L424T
    PATTERNS = [
        Pattern("CF (very weak)", r"[A-Z]{6}[0-9]{2}[A-E,H,L,M,P,R-T][0-9]{2}[A-Z0-9]{5}", 0.5),
    ]
    CONTEXT = ["Codice fiscale", "codice fiscale"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="IT_CF",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
