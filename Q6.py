n = int(input("Enter number: "))
a = int(input("Enter first digit: "))
b = int(input("Enter second digit: "))

count_a = 0
count_b = 0

if n == 0:
    if a == 0:
        count_a = 1
    if b == 0:
        count_b = 1

while n > 0:
    digit = n % 10

    if digit == a:
        count_a += 1

    if digit == b:
        count_b += 1
    n //= 10

print(abs(count_a - count_b))