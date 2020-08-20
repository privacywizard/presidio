from presidio_analyzer import Pattern, PatternRecognizer


class SpainDNIRecognizer(PatternRecognizer):
    """
    Recognizes Documento Nacional de Identidad using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Documento Nacional de Identidad are a weak match, e.g., 99999999-R
    PATTERNS = [
        Pattern("DNI (very weak)", r"[0-9,X,M,L,K,Y][0-9]{7}-[A-Z]", 0.5),
    ]
    CONTEXT = ["Documento Nacional de Identidad", "documento nacional de identidad"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="ES_DNI",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
