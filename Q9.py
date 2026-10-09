
from math import isqrt

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False

    return True

n = int(input("Enter n: "))
candidate = n + 1

while not is_prime(candidate):
    candidate += 1

print("Next prime =", candidate)
