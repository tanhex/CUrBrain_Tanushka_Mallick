
from math import gcd

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

result = arr[0]

for i in range(1, n):
    result = gcd(result, arr[i])

print("GCD =", result)
