class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []
        
        for x in nums1:
            if x in nums2:
                if x not in res:
                    res.append(x)
        for y in nums2:
            if y in nums1:
                if y not in res:
                    res.append(y)
        return res