from presidio_analyzer import Pattern, PatternRecognizer


class AustriaNIMRecognizer(PatternRecognizer):
    """
    Recognizes Austria National identification number using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: National identification number - Zentrales Melderegister (Central Register of Residents - CRR) are a weak match, e.g., 000247681888
    PATTERNS = [
        Pattern("ZMR-Zahl (very weak)", r"[0-9]{12}", 0.5),
    ]
    CONTEXT = ["national identification number", "Zentrales Melderegister", "Central Register of Residents - CRR"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="AT_ZMR_Zahl",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
