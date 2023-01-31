class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        count = 0
        mp = collections.defaultdict(int)
        for a in nums1:
            for b in nums2:
                mp[(a+b)]+=1
        
        for c in nums3:
            for d in nums4:
                count+=mp[-(c+d)]
        
        return count