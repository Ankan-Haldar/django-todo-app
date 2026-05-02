class Solution:
    def search(self, arr, x):
        # code here
        for i in range(0,len(arr)):
            if arr[i]==x:
                return i
                break
        return -1