class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        globmax, globmin = nums[0],nums[0]
        curmax,curmin = 0,0
        total = 0
        
        for n in nums:
            curmax = max(curmax+n,n)
            curmin = min(curmin+n,n)
            total +=n
            globmax = max(globmax,curmax)
            globmin = min(globmin,curmin)
        
        return max(globmax,total-globmin) if globmax>0 else globmax
    