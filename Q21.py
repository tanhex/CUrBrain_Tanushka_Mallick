def delete_value(arr, target):
    n = len(arr)
    index = -1

    for i in range(n):
        if arr[i] == target:
            index = i
            break

    if index != -1:
        for i in range(index, n - 1):
            arr[i] = arr[i + 1]

        del arr[-1]


arr = [10, 20, 30, 20, 40]
target = 20

delete_value(arr, target)
print(arr)