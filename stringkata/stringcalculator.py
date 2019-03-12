
import re as regex


class IllegalArgumentError(ValueError):
    pass


class StringCalculator():

    def add(self, text):

        if len(text) == 0:
            return 0

        num_array = self.get_number_array(text)

        self.check_for_negative_numbers(num_array)

        return sum(num_array)

    def get_number_array(self, text):

        custom_delimiter = ",|\n"
        if text.startswith("//"):
            custom_delimiter = text[2: text.index("\n")]
            text = text[text.index("\n") + 1:]

        split_text = regex.compile(custom_delimiter).split(text)
        num_array = list(map(lambda s: int(s), split_text))

        return num_array

    def check_for_negative_numbers(self, num_array):
        for number in num_array:
            if number < 0:
                raise IllegalArgumentError("should not contain negative numbers")
