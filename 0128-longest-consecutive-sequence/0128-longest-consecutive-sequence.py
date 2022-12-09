class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mapp = dict()
        res = 0
        for n in nums:
            if n not in mapp:
                left = mapp.get(n-1,0)
                right = mapp.get(n+1,0)
                cur = left + 1 + right
                res = max(res, cur)
                mapp[n] = cur
                mapp[n-left] = cur
                mapp[n+right] = cur
        return res
        
        
        