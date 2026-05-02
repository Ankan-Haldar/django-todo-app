def max_product_triplet(arr):
    first = second = third = float("-inf")   # 3 largest
    min1 = min2 = float("inf")               # 2 smallest

    for num in arr:
        # update largest 3
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num

        # update smallest 2
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    # two possible answers
    option1 = first * second * third
    option2 = first * min1 * min2

    return max(option1, option2)

arr = [1, -4, 3, -6, 7, 0, 10, 20, 30]
result = max_product_triplet(arr)
print(result)