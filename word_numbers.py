"""
Constraints/etc.:

- handle inputs ranging from 0 to 1000000, inclusive
- don't worry about exception handling
- input is a number, not a string representing a number
"""

import math

class WordNumbers():

    @staticmethod
    def get_digit_count(number):
        if number > 0:
            return int(math.log10(number))+1
        elif number == 0:
            return 1

    @staticmethod
    def convert(number):
        return "one"