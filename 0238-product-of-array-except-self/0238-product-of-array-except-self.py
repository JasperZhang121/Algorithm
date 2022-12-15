class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pro = 1
        zero = False
        c = 0 
        
        for x in nums:
            if x == 0:
                pro*=1
                zero = True
                c+=1
            else:
                pro*=x
            
        res = [0]*len(nums)
        
        for i in range(len(nums)):
            if zero:
                if nums[i] == 0 and c==1:
                    res[i] = pro
            else:
                res[i] = pro//nums[i]
            
        return res