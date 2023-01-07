class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res,cur = 0,0
        mp = {0:1}
        for n in nums:
            cur += n
            diff = cur - k 
            res += mp.get(diff,0)
            mp[cur] = 1 + mp.get(cur,0)
        return res
            