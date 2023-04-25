class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        
        boo = False
        
        for i in range(1,len(nums)):
            
            cur, pre = nums[i], nums[i-1]
            
            if pre == cur:
                boo = True
                
            else:
                if boo == True:
                    boo = False
                else:
                    return pre
                
        if boo == False:
            return nums[-1]
            