# Problem statement:
# return the value of the first duplicate in a list of integers
# return null if there are no dupes

import random
from timeit import Timer

ITERATIONS = 1000

nums1 = [1, 4, 8, 3, 7, 1, 2, 6, 19, -4]
nums2 = [0, 4, 8, 3, 7, 1, 2, 6, 19, -4]
nums3 = [-4, 0, 4, 8, 3, 7, 1, 2, 6, 19, -4]
nums4 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
nums_no_dupes = [x for x in range(1000)]
nums_dupe = [-1] + [x for x in range(10000)] + [-1]
middle_dupes = [x for x in range(1001,2001)] + [-1,-1] + [x for x in range(1000)]

# better simulate "real" data by shuffling a dupe into a random list
# run several times for best results, as dupe location will vary between runs
random_nums = [random.randint(0, 10000) for _ in range (9999)]
duplicate = [random.choice(random_nums) for _ in range(1)]
mixed_data = random_nums + duplicate
random.shuffle(mixed_data)

def first_dupe(numbers):
    if len(numbers) == len(set(numbers)):
        return None  # all values in the list are unique
    for i, num in enumerate(numbers):
        search_list = numbers[i + 1:]
        for s in search_list:
            if num == s:
                return num

def first_dupe_v2(numbers):
    size = len(numbers)
    for i in range(size):
        for j in range(i + 1, size):
            if numbers[i] == numbers[j]:
                return numbers[i]
    return None

def first_dupe_v3(numbers):
    seen = set()
    for number in numbers:
        old_length = len(seen)
        seen.add(number)
        if len(seen) == old_length:  # dupes don't add to the length
            return number
    return None

if __name__ == '__main__':
    # use a var so we can switch out test sets easily
    test_data = mixed_data

    t = Timer("first_dupe(test_data)", "from __main__ import first_dupe, test_data")
    print(t.timeit(number=ITERATIONS))

    t = Timer("first_dupe_v2(test_data)", "from __main__ import first_dupe_v2, test_data")
    print(t.timeit(number=ITERATIONS))

    t = Timer("first_dupe_v3(test_data)", "from __main__ import first_dupe_v3, test_data")
    print(t.timeit(number=ITERATIONS))