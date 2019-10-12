"""
run program with this command:

python word_numbers.py <number>

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
        total_count = self.get_digit_count(number)
        if total_count == 1:
            return self.single_digit_numbers[number]
        elif total_count == 2:
            return self.convert_two_digit(number)
        elif total_count == 3:
            return self.convert_three_digit(number)
        elif total_count in [4, 5, 6]:
            thousands_number = int(str(number)[:-3])
            remaining_numbers = int(str(number)[-3:])
            thousands_count = self.get_digit_count(thousands_number)
            if thousands_count == 1:
                output = self.single_digit_numbers[thousands_number]
            elif thousands_count == 2:
                output = self.convert_two_digit(thousands_number)
            else:
                output = self.convert_three_digit(thousands_number)
            
            output += " thousand"

            if remaining_numbers == 0:
                return output

            if self.get_digit_count(remaining_numbers) == 1:
                output += " " + self.single_digit_numbers[remaining_numbers]
            elif self.get_digit_count(remaining_numbers) == 2:
                output += " " + self.convert_two_digit(remaining_numbers)
            else:
                output += " " + self.convert_three_digit(remaining_numbers)
            return output

        elif total_count in [7]:
            return "one million"

    def convert_three_digit(self, number):
        hundreds_number = int(str(number)[:-2])
        remaining_numbers = int(str(number)[-2:])
        output = self.single_digit_numbers[hundreds_number] + " hundred"
        if remaining_numbers != 0:
            if self.get_digit_count(remaining_numbers) == 1:
                output += " " + self.single_digit_numbers[remaining_numbers]
            else:
                output += " " + self.convert_two_digit(remaining_numbers)
        return output

    def convert_two_digit(self, number):
        if number in self.double_digit_numbers.keys():
            return self.double_digit_numbers[number]
        elif number != 0:
            return self.double_digit_numbers[number // 10 * 10] + " " + \
                self.single_digit_numbers[number % 10]
        else:
            return ""

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