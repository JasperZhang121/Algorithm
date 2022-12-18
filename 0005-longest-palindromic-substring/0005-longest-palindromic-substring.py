class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(s,l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1;
                r+=1
            return r-l-1
        
        if s==None or len(s) < 1:
            return ""
        
        start, end = 0,0
        for i in range(len(s)):
            l1=expandFromCenter(s,i,i)
            l2=expandFromCenter(s,i,i+1)
            lll = max(l1,l2)
            if lll>end-start:
                start = i-(lll-1)//2
                end = i+ lll//2
        m=end+1        
        return s[start:m]        