# Problem statement:
# return the value of the first duplicate in a list of integers
# return null if there are no dupes

nums1 = [1, 4, 8, 3, 7, 1, 2, 6, 19, -4]
nums2 = [0, 4, 8, 3, 7, 1, 2, 6, 19, -4]
nums3 = [-4, 0, 4, 8, 3, 7, 1, 2, 6, 19, -4]
nums4 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

def first_dupe(numbers):
    if len(numbers) == len(set(numbers)):
        return None  # all values in the list are unique
    for i, num in enumerate(numbers):
        search_list = numbers[i + 1:]
        for s in search_list:
            if num == s:
                return num

print('expect 1, get ' + str(first_dupe(nums1)))
print('expect None, get ' + str(first_dupe(nums2)))
print('expect -4, get ' + str(first_dupe(nums3)))
print('expect 3, get ' + str(first_dupe(nums4)))
