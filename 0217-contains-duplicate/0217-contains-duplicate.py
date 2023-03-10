class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        n = Counter(nums)
        
        for x,y in n.items():
            if y > 1:
                return True
            
        return False