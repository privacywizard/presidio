from presidio_analyzer import Pattern, PatternRecognizer


class IMEIRecognizer(PatternRecognizer):
    """
    Recognizes common imei numbers using regex + checksum

    """

    # pylint: disable=line-too-long
    PATTERNS = [
        Pattern(
            "IMEI check",
            r"\d{15}",  # noqa: E501
            0.5,
        ),
    ]

    CONTEXT = [
        "imei",
        "International Mobile Equipment Identity",
    ]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="IMEI",
        replacement_pairs=None,
    ):
        """
            :param replacement_pairs: list of tuples to replace in the string.
                ( default: [("-", ""), (" ", "")] )
                i.e. remove dashes and spaces from the string during recognition.
        """
        self.replacement_pairs = replacement_pairs \
            if replacement_pairs \
            else [("-", ""), (" ", "")]
        context = context if context else self.CONTEXT
        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )

    def validate_result(self, pattern_text):
        sanitized_value = self.__sanitize_value(pattern_text, self.replacement_pairs)
        checksum = self.__isValidEMEI(sanitized_value)

        return checksum

    @staticmethod
    def __sanitize_value(text, replacement_pairs):
        for search_string, replacement_string in replacement_pairs:
            text = text.replace(search_string, replacement_string)
        return text

    def __sumDig(self,  n ): 
        a = 0
        while n > 0: 
            a = a + n % 10
            n = int(n / 10)
        return a 

    # Returns True if n is valid EMEI 
    def __isValidEMEI(self, n): 

        # Converting the number into 
        # Sting for finding length 
        s = str(n) 
        n = int(n)
        l = len(s) 
    
        # If length is not 15 then IMEI is Invalid 
        if l != 15: 
            return False

        d = 0
        sum = 0
        for i in range(15, 0, -1): 
            d = (int)(n % 10) 
            if i % 2 == 0: 
    
                # Doubling every alternate digit 
                d = 2 * d 
    
            # Finding sum of the digits 
            sum = sum + self.__sumDig(d) 
            n = n / 10
        return (sum % 10 == 0) 
