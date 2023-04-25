class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        coun = Counter(nums)
        
        for x ,y in coun.items():
            while y>2:
                nums.remove(x)
                y-=1
        
        return len(nums)