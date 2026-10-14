
def modular_addition(arr):
    MOD = 10**9 + 7
    result = 0

    for value in arr:
        result = (result + value) % MOD

    return result


arr = [1000000000, 1000000000, 1000000000]
print(modular_addition(arr))
