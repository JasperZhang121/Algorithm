class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        le, ri = 0, len(nums)-1
        
        while le<=ri:
            mid = (le+ri)//2
            
            if nums[mid]<target:
                le = mid+1
            elif nums[mid]>target:
                ri = mid-1
            else:
                return mid
        return -1 