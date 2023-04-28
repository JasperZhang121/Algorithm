class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m
        while a<len(nums1):
            nums1[a] = nums2[m+n-a-1]
            a+=1
        
        nums1.sort()
        