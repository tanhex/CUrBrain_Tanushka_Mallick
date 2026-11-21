def suffix_sum(arr):
    total = 0

    for i in range(len(arr) - 1, -1, -1):
        current = arr[i]
        arr[i] = total
        total += current


arr = [10, 4, 8, 3]

suffix_sum(arr)
print(arr)