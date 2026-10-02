n = int(input("Enter number: "))
sum_digits = 0
product = 1

while n > 0:
    digit = n % 10
    sum_digits += digit
    product *= digit
    n //= 10

print(product - sum_digits)