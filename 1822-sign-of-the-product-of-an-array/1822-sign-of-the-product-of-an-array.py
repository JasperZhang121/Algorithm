class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        count = 0
        
        for x in nums:
            if x<0:
                count+=1
            elif x==0:
                return 0 
            
        return -1 if count%2 else 1