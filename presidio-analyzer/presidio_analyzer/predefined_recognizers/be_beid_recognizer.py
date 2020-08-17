from presidio_analyzer import Pattern, PatternRecognizer


class BelgiumBEIDRecognizer(PatternRecognizer):
    """
    Recognizes Belgium identification number of the National Register using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: new national identification number are a weak match, e.g., 1234030869
    PATTERNS = [
        Pattern("BEID (very weak)", r"[0-9]{2}\.?[0-9]{2}\.?[0-9]{2}-[0-9]{3}\.?[0-9]{2}", 0.5),
    ]
    CONTEXT = ["Identification number of the National Register", "SIS", "social security"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="BE_ID",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
