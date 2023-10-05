from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = []
        n = len(nums)/3
        temp = Counter(nums)
        
        for k,v in temp.items():
            if v>n:
                res.append(k)
                
        return res
            
        