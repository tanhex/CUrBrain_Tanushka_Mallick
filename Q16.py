def second_highest(scores):
    highest = None
    second = None

    for score in scores:
        if highest is None or score > highest:
            second = highest
            highest = score
        elif score != highest and (second is None or score > second):
            second = score

    if second is None:
        return -1

    return second


scores = list(map(int, input().split()))

print(second_highest(scores))