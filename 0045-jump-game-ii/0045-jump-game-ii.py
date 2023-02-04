class Solution:
    def jump(self, nums: List[int]) -> int:

        
        n = len(nums)
        jump_count = 0
        max_reach = 0
        # initialize the current reachable index to 0
        reach = 0
        for i in range(n-1):
            max_reach = max(max_reach, i + nums[i])
            # if we have reached the last index we can reach from the current position,
            # update the jump count and the current reachable index
            if i == reach:
                jump_count += 1
                reach = max_reach
        # return the jump count
        return jump_count