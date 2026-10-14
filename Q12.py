
def modulo_power(base, power, MOD):
    result = 1 % MOD

    for i in range(power):
        result = (result * base) % MOD

    return result


base = 2
power = 10
MOD = 1000

print(modulo_power(base, power, MOD))
