class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        d = {}
        low, res = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            res = max(i - low + 1, res)
        return res
            
            
           
                
            