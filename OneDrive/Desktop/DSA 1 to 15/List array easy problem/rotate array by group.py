def reversegroup(arr,k):
    n=len(arr)
    for i in range(0,n,k):
        left=i
        right=i+k-1
        if right>=n:
            right=n-1
        # now reverse current group
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
arr = [1,2,3,4,5,6,7,8]
k = 3
reversegroup(arr,k)
print(arr)