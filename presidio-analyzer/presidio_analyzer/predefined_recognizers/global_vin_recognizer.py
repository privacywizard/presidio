from presidio_analyzer import Pattern, PatternRecognizer


class GlobalVINRecognizer(PatternRecognizer):
    """
    Recognizes Estonia Isikukood using regex
    """

    # pylint: disable=line-too-long,abstract-method
    # Weak pattern: new national identification number are a weak match, e.g., 1234030869
    PATTERNS = [
        Pattern("VEHICLE IDENTIFICATION NUMBER (weak)", r"^(?=.*[0-9])(?=.*[A-z])[0-9A-z-]{17}$", 0.5),
    ]
    CONTEXT = ["VEHICLE IDENTIFICATION NUMBER", "VIN", "VEHICLE_IDENTIFICATION_NUMBER"]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="GLOBAL_VIN",
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
