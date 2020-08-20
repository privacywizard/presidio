from presidio_analyzer import Pattern, PatternRecognizer


class GermanySteuerIDRecognizer(PatternRecognizer):
    """
    Recognizes Steuer-Identifikationsnummer using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: Steuer-Identifikationsnummer are a weak match, e.g., 316/5756/0463
    PATTERNS = [
        Pattern("SteuerID (very weak)", r"[0-9]{3}\/?[0-9]{4}\/?[0-9]{4}", 0.5),
    ]
    CONTEXT = ["Steuer-Identifikationsnummer", "steuer-identifikationsnummer"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="DE_SteuerID",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
