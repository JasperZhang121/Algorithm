class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==0:
            return [-1,-1]
        l = -1;
        r = -1;
        for i in range(len(nums)):
            if nums[i] == target:
                if l==-1:
                    l = i
                else:
                    r = i
        if l!=-1 and r!=-1:
            return [l,r]
        elif l!=-1 and r==-1:
            return [l,l]
        else:
            return [-1,-1]