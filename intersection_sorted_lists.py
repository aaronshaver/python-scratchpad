b = [1, 2, 3, 4, 5]
a = [3, 4, 5, 6, 7, 8, 9, 10]

i = 0
j = 0
common = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        common.append(a[i])
        i += 1
        j += 1

print(common)
