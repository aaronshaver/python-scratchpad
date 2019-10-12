"""
Constraints/etc.:

- handle inputs ranging from 0 to 1000000, inclusive
- don't worry about exception handling
- input is a number, not a string representing a number
"""

import math

class WordNumbers():

    def get_digit_count(self, number):
        if number > 0:
            return int(math.log10(number))+1
        elif number == 0:
            return 1

    def convert(self, number):
        if self.get_digit_count(number) == 1:
            return self.single_digit_numbers[number]

    single_digit_numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }