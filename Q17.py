sales = list(map(int, input().split()))

freq = {}

for i in sales:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

max_freq = 0
result = 0

for i in freq:
    if freq[i] > max_freq:
        max_freq = freq[i]
        result = i
    elif freq[i] == max_freq and i < result:
        result = i

print(result)