# The point of this is that the output has a repeating pattern
# as the exponent increases

a = 2
mod = 11
for n in range(50):
    print((a ** n) % mod)
