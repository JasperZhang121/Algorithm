class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if target not in nums:
            return -1
        else:
            i=0
            while i < len(nums):
                if nums[i]==target:
                    return i
                i+=1