nums=[1,2,3,4,5,6]

n=len(nums)

temp=nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]
    nums[i]=temp
print(nums)