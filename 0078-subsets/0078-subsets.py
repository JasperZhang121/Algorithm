class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []
        i=0
        def dfs(nums):
            
            if len(nums)==0:
                return    
            for x in nums: 
                path.append(x)
                temp = path.copy()
                res.append(temp)
                nums = nums[i+1:]
                dfs(nums)
                path.pop()
                
        dfs(nums)
        res.append([])
        return res
            