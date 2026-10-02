n = int(input("Enter number: "))
digits = []
while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        digits.append(0)
    else:
        digits.append(digit)
    n //= 10

digits.reverse()
print(digits)