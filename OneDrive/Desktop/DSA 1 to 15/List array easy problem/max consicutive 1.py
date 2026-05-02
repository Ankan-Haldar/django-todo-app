def max_consecutive_ones(arr):
    count=0
    maxi=0
    for i in arr:
        if i==1:
            count+=1
            maxi=max(maxi,count)
        else:
            count=0
    return maxi

arr = [1,1,0,1,1,1,0,1]
print(max_consecutive_ones(arr))