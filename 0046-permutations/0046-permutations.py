class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def bt(temp):
            if len(temp) == len(nums):
                res.append(temp[:])
                return 
            for x in nums:
                if x not in temp:
                    temp.append(x)
                    bt(temp)
                    temp.remove(x)
        
        bt([])
        return res            
        
            
        