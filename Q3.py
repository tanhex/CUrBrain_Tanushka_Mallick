n = int(input("Enter number: "))

if n < 0:
    reverse = -1
    x = abs(n)
else:
    reverse = 1
    x = n

original = x
rev = 0

while x > 0:
    digit = x % 10
    rev = rev * 10 + digit
    x //= 10

rev *= reverse

if n >= 0 and n == rev:
    print(n)
else:
    print(n + rev)