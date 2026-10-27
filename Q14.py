def threshold_filter(sales, threshold):
    result = []

    for value in sales:
        if value >= threshold:
            result.append(value)

    return result


sales = list(map(int, input().split()))
threshold = int(input())

print(threshold_filter(sales, threshold))