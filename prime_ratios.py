"""
Demonstrates that primes ending in 1, 3, 7, 9 approach 25% each
as n approaches infinity (where n is number of primes to examine
"""
import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(n):
    count = {1: 0, 3: 0, 7: 0, 9: 0}
    primes_found = 0
    num = 3
    while primes_found < n:
        if num % 10 in count and is_prime(num):
            count[num % 10] += 1
            primes_found += 1
        num += 2
    return count

def main():
    if len(sys.argv) != 2:
        print("Usage: python prime_ratios.py <numberOfPrimes>")
        return
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    counts = count_primes(n)
    total = sum(counts.values())
    for digit in sorted(counts.keys()):
        percent = (counts[digit] / total) * 100
        print(f"{digit}: {percent:.3f}%")

if __name__ == "__main__":
    main()
