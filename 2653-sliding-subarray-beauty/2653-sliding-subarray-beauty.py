from sortedcontainers import SortedList 

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        vals = SortedList()
        for i, v in enumerate(nums): 
            vals.add(v)
            if i >= k:
                vals.remove(nums[i-k])
            if i >= k-1: 
                ans.append(min(0, vals[x-1]))
        return ans 
        