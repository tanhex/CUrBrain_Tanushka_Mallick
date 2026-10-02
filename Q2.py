n = int(input("Enter number: "))

sign = -1 if n < 0 else 1
n = abs(n)

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

reverse *= sign

print(reverse * 2)