n = int(input("Enter number: "))
x = abs(n)

if x == 0:
    count = 1
else:
    count = 0
    while x > 0:
        count += 1
        x //= 10

print(count % 2 == 0)