class Solution:
    def partitionString(self, s: str) -> int:
        
        cur,count = "",0
        
        for x in s:
            if x not in cur:
                cur += x 
            else: 
                count +=1
                cur = x
                
        if cur!="":
            count+=1
        
        return count
            