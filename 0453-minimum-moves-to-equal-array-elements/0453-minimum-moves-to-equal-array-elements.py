class Solution:
    def minMoves(self, nums: List[int]) -> int:
        
        nums.sort()
        c = 0
        for i in range(len(nums)-1,0,-1):
            c += nums[i]-nums[0]
        return c