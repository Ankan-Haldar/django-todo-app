def maxprofit(arr):
    n=len(arr)
    min_price=arr[0]
    max_profit=0

    for i in range(n-1):
        if arr[i]<min_price:
            min_price=arr[i]
        else:
            profit=arr[i]-min_price
            if profit>max_profit:
                max_profit=profit
    return max_profit
arr=[7, 10, 1, 3, 6, 9, 2]
print(maxprofit(arr))