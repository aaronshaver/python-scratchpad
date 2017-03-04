def sum(n):
    if n <= 0: return 0
    return n + sum(n-1)

def sum2(n):
    return n * (n + 1) // 2

for i in range(10):
    print("sum(" + str(i) + ") == " + str(sum(i)))

for i in range(10):
    print("sum2(" + str(i) + ") == " + str(sum2(i)))
