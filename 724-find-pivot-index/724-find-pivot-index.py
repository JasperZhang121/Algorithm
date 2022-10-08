class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        left_sum = 0
        for index in range(len(nums)):                
            right_sum = total - left_sum - nums[index]
            if left_sum == right_sum:
                return index
            left_sum += nums[index]
        return -1