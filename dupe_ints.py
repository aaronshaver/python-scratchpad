# Problem statement:
# return the value of the first duplicate in a list of integers
# return null if there are no dupes

import time

nums1 = [1, 4, 8, 3, 7, 1, 2, 6, 19, -4]
nums2 = [0, 4, 8, 3, 7, 1, 2, 6, 19, -4]
nums3 = [-4, 0, 4, 8, 3, 7, 1, 2, 6, 19, -4]
nums4 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
nums_no_dupes = [x for x in range(1000)]
nums_dupe = [-1] + [x for x in range(10000)] + [-1]

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

# print('expect 1, get ' + str(first_dupe(nums1)))
# print('expect None, get ' + str(first_dupe(nums2)))
# print('expect -4, get ' + str(first_dupe(nums3)))
# print('expect 3, get ' + str(first_dupe(nums4)))

# print()

# print('expect 1, get ' + str(first_dupe_v2(nums1)))
# print('expect None, get ' + str(first_dupe_v2(nums2)))
# print('expect -4, get ' + str(first_dupe_v2(nums3)))
# print('expect 3, get ' + str(first_dupe_v2(nums4)))

if __name__ == '__main__':
    from timeit import Timer
    test_data = nums_dupe  # so we can switch out test sets easily
    t = Timer("first_dupe(test_data)", "from __main__ import first_dupe, test_data")
    print(t.timeit(number=1000))
    t = Timer("first_dupe_v2(test_data)", "from __main__ import first_dupe_v2, test_data")
    print(t.timeit(number=1000))
