class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        l = False
        r = False 
        
        for i in range(n):
            if i==0:
                if nums[i]>-1:
                    l = True
                if i==n-1:
                    r = True
                else:
                    if nums[i]>nums[i+1]:
                        r = True
                
            else:
                if nums[i]>nums[i-1]:
                    l = True
                if i<n-1:
                    if nums[i]>nums[i+1]:
                        r = True
                else: 
                    r = True
    
            if l == True and r == True:
                return i
        return 0