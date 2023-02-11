class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start,fq,mx,length = 0,{},0,0
        
        for end in range(len(s)):
            fq[s[end]] =  fq.get(s[end],0)+1
            mx = max (mx,fq[s[end]])
            valid = (end+1-start-mx<=k)
            
            if not valid:
                fq[s[start]] -=1
                start+=1
            length = end+1-start
            
        return length