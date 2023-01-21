class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        res,n = 0,len(nums)
        nums.sort()
        for i in range(n):
            l,r = i+1,n-1
            
            while l<r:
                summ = nums[i]+nums[l]+nums[r]
                if summ<target:
                    res += r-l
                    l += 1
                else:
                    r -= 1           
        return res
                    