"""
Constraints/etc.:

- handle inputs ranging from 0 to 1000000, inclusive
- don't worry about exception handling
- input is a number, not a string representing a number
"""

import math
import sys

class WordNumbers():

    def get_digit_count(self, number):
        if number > 0:
            return int(math.log10(number))+1
        elif number == 0:
            return 1

    def convert(self, number):
        count = self.get_digit_count(number)
        if count == 1:
            return self.single_digit_numbers[number]
        elif count == 2:
            if number in self.double_digit_numbers.keys():
                return self.double_digit_numbers[number]
            else:
                return self.double_digit_numbers[number // 10 * 10] + " " + \
                    self.single_digit_numbers[number % 10]
        elif count in [4, 5]:
            thousands_number = int(str(number)[:-3])
            if self.get_digit_count(thousands_number) == 2:
                return self.double_digit_numbers[thousands_number] + " thousand"
            else:
                return self.single_digit_numbers[thousands_number] + " thousand"
        elif count in [7]:
            return "one million"

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

    double_digit_numbers = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

if __name__ == "__main__":
    converter = WordNumbers()
    print(converter.convert(int(sys.argv[1])))