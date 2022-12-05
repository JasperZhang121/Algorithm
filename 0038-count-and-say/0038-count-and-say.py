class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            s = self.countAndSay(n-1)
            
            i,j,ans = 0,0, ""
            while j<len(s):
                if s[i]==s[j]:
                    if j == len(s)-1:
                        if i!=j:
                            ans +=str(j-i+1)+s[i]
                        else:
                            ans +="1"+s[i]
                    j+=1
                else:
                    ans += str(j-i)+s[i]
                    i=j
            return ans