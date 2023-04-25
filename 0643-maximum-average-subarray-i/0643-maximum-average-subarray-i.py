class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        i,j,n=k,0,len(nums)
        m=s=sum(nums[:k])
        while i<n:
            s+=nums[i]-nums[j]
            m=max(m,s)
            i+=1
            j+=1
        return m/k