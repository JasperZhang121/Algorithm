class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        n = columnTitle; res = 0; c=0
        
        for i in range(len(n)-1,-1,-1):
            
            c = len(n)-i

            res += (ord(n[i])-ord('A')+1)*(26**(c-1))
        

        return res
        