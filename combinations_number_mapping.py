# task: for a number like 258
# return all combinations of words made of letters
# where each number corresponds to letters
# e.g. 2-abc, 3-def, 4-ghi, 5-jkl, 6-mno, 7-pqr, 8-stu, 9-vwx
# so 258 could be ajs or alu or cks, etc.
# original problem was a number, but going to assume string
# to get the heart of the problem
# we could do the % 10 thing to get each digit, but meh

mappings = {}
mappings['2'] = ['a', 'b', 'c']
mappings['3'] = ['d', 'e', 'f']
mappings['4'] = ['g', 'h', 'i']

def convert(num):
    print(num)
    combinations = []
    for letter in mappings[num[0]]:
        for letter2 in mappings[num[1]]:
            for letter3 in mappings[num[2]]:
                combinations.append(letter + letter2 + letter3)
    return combinations

print('234:')
print(convert('234'))