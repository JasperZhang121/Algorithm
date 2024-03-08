class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        sm = 0
        mx = max(c.values())
        for x in c.values():
            if x==mx:
                sm+=x
        return sm