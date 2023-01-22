class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        n,j,res,count = len(nums),0,0,0
        
        for i in range(n):
            while j<n and (nums[j]==1 or (nums[j]==0 and count<k)):
                if nums[j]==0:
                    count+=1
                j+=1
            res = max(res,j-i)
            if nums[i]==0:
                count-=1
        return res
    