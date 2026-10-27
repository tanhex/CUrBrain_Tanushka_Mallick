def minimum_absolute_value(arr):
    minimum = arr[0]

    for value in arr[1:]:
        if abs(value) < abs(minimum):
            minimum = value

    return minimum


arr = list(map(int, input().split()))

print(minimum_absolute_value(arr))