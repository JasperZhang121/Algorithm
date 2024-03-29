class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        res = []
        if a==0:
            res = [b*x+c for x in nums]
            if b<0:
                res.reverse()
        else:
            flag = a>0
            mid = -b/(2*a)
            
            l,r = 0, len(nums)-1
        
            while l<=r:
                if abs(mid-nums[l])>abs(mid-nums[r]):
                    res.append(a*nums[l]*nums[l]+b*nums[l]+c)
                    l+=1
                else:
                    res.append(a*nums[r]*nums[r]+b*nums[r]+c)
                    r-=1
            if flag: res.reverse()
        return res
            
        