class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        res,n = [],len(nums)
        if n<4: return res
        
        nums.sort()
        for i in range(n):
            if nums[i]*4 > target: break
            if nums[i]+nums[-1]*3<target: continue
                
            for j in range(i+1,n):
                if nums[i]+nums[j]*3 > target: break
                if nums[i]+ nums[j]+nums[-1]*2<target: continue   
                if i>0 and nums[i]==nums[i-1]: continue
                if j>i+1 and nums[j]==nums[j-1]: continue
                
                l,r = j+1,n-1
                
                while l<r:
                    summ = nums[i]+nums[j]+nums[l]+nums[r]
                    if summ>target:
                        r-=1
                    elif summ<target:
                        l+=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
        return res
                        
            
        