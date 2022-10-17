class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        res = []
        for x in n1.keys():
            if x in n2.keys():
                    y = n1[x]
                    z = n2[x]
                    if y<z:
                        while y>0:
                            res.append(x)
                            y-=1
                    else:
                        while z>0:
                            res.append(x)
                            z-=1
        return res
                