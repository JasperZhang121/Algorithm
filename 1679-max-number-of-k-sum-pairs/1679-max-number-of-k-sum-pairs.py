class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        b = {}
        ans = 0
        for x in nums:
            if k - x in b and b[k - x] > 0:
                ans += 1
                b[k - x] -= 1  
            elif x not in b:
                b[x] = 1
            else:
                b[x] += 1
        
        return ans
            
        