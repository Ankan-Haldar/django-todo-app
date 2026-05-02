def webarr(arr):
    arr.sort()
    n=len(arr)
    for i in range(0,n-1,2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
arr=[1,2,3,4,5,6]
print(webarr(arr))
arr=[4,2,5,6,7,9]
print(webarr(arr))
 