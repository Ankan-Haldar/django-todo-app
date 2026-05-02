class Solution:
    def largest(self, arr):
        # code here
        largest=arr[0]
        n=len(arr)
        for i in range(0,n):
            largest=max(largest,arr[i])
        return largest
        
