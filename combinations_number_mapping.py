# task: for a number like 258
# return all combinations of words made of letters
# where each number corresponds to letters
# e.g. 2-abc, 3-def, 4-ghi, 5-jkl, 6-mno, 7-pqr, 8-stu, 9-vwx
# so 258 could be ajs or alu or cks, etc.

# library function method (some Stack Overflow code, some of my code)
import itertools
sets = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
combinations = list(itertools.product(*sets))
formatted = [''.join(combo) for combo in combinations]
print(formatted)

# recursive solution not using a library function (not my code!)
combinations2 = []

def combine(terms, accum):
    last = (len(terms) == 1)
    n = len(terms[0])
    for i in range(n):
        item = accum + terms[0][i]
        if last:
            combinations2.append(item)
        else:
            combine(terms[1:], item)

combine([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']],'')
print(combinations2)

# noodling around:

# mappings = {}
# mappings['2'] = ['a', 'b', 'c']
# mappings['3'] = ['d', 'e', 'f']
# mappings['4'] = ['g', 'h', 'i']

# def convert(num):
#     print(num)
#     combinations = []
#     for letter in mappings[num[0]]:
#         for letter2 in mappings[num[1]]:
#             for letter3 in mappings[num[2]]:
#                 combinations.append(letter + letter2 + letter3)
#     return combinations

# print('234:')
# print(convert('234'))