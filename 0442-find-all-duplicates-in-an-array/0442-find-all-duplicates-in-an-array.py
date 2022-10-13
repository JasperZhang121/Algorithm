class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        lis = []
        c = Counter(nums)        
        for x,y in c.items():
            if y!=1:
                lis.append(x)
        return lis
                