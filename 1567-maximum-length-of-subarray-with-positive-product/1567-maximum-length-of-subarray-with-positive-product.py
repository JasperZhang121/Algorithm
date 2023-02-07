class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
            pos = neg = ans = 0
    
            for n in nums:
                if n > 0:
                    pos = 1 + pos
                    neg = 1 + neg if neg else 0
                elif n <0:
                    pos, neg = 1 + neg if neg else 0, 1 + pos
                else:
                    pos, neg = 0,0
                ans = max(ans, pos)

            return ans
