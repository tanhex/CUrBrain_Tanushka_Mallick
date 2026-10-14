
def divisible_prefix_subarray(arr, k):
    prefix_sum = 0
    k = abs(k)

    for value in arr:
        prefix_sum += value

        if prefix_sum % k == 0:
            return True

    return False


arr = [4, 2, 9]
k = 3

print(divisible_prefix_subarray(arr, k))
