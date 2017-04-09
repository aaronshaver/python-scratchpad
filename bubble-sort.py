a = list(reversed([x for x in range(100)]))

print(a)

while True:
    swaps = 0
    for i, item in enumerate(a):
        if i < len(a) - 1:  # don't compare past end of list
            if item > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swaps += 1
    if swaps == 0:
        break

print(a)
