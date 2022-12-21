class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res,i,j = 0,0,len(height)-1
        while i<j:
            res = max(res,(j-i)*(min(height[j],height[i])))
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return res
            
         
        