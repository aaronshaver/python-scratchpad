def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
