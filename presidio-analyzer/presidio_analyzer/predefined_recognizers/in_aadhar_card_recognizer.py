import re
from presidio_analyzer import Pattern, PatternRecognizer


class AadharRecognizer(PatternRecognizer):
    """
    Recognizes common aadhar card numbers using regex

    """

    # pylint: disable=line-too-long
    PATTERNS = [
        Pattern(
            "AadharCard check",
            r"\d[2-9]{1}[0-9]{2}\s[0-9]{4}\s[0-9]{4}",  # noqa: E501
            0.5,
        ),
    ]

    CONTEXT = [
        "aadhar",
        "aadhar card",
    ]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="AADHAR_CARD",
        replacement_pairs=None,
    ):
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )

    def validate_result(self, pattern_text):
        checksum = re.search("\d[2-9]{1}[0-9]{2}\s[0-9]{4}\s[0-9]{4}", pattern_text)
        return checksum != None
