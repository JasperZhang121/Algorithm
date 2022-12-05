class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            s = self.countAndSay(n-1)
            ans = ""
            i,j=0,0
            while i<len(s):
                while j<len(s) and s[i]==s[j]:
                    j+=1
                ans+=str(j-i)+s[i]
                i = j-1
                i+=1
            return ans 