def maxprofit(arr):
    n=len(arr)
    profit=0
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            profit+=arr[i]-arr[i-1]
    return profit
arr=[100, 180, 260, 310, 40, 535, 695]
print(maxprofit(arr))