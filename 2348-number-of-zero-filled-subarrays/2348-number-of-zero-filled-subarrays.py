class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        res, num = 0,0
        for x in nums:
            if x==0:
                num += 1
            else:
                num = 0
            res += num
            
        return res