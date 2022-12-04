class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)==1:return True
        
        maxi = 0
        for i in range(len(nums)-1):
            
            if i>maxi:
                return False
            
            maxi = max(maxi, i+nums[i])
            if maxi >= len(nums)-1:
                return True
           
            
        return False
            