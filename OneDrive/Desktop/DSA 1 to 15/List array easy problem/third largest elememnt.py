nums=[1,4,2,3,5,34,7,54,8,9,0,3,4,5,6,7,8,99,3]

largest=float("-inf")
snd_largest=float("-inf")
third=float("-inf")
n=len(nums)
for i in range(0,n):
    if nums[i]>largest:
        third=snd_largest
        snd_largest=largest
        largest=nums[i]
    elif nums[i]>snd_largest and nums[i]!=largest:
        third=snd_largest
        snd_largest=nums[i]
    elif nums[i]>third and nums[i]!=largest and nums[i]!=snd_largest:
        third=nums[i]
if third==float("-inf"):
    print("Not enough distinct element")
print (third)