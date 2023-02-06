class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        mid = len(nums)//2
        res = []
        
        for i in range(mid):
            res.append(nums[i])
            res.append(nums[i+mid])
        
        return res