class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s == None or len(s)==0 or s[0]=='0':
            return 0
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(1,len(s),1):
            if s[i]!='0':
                dp[i+1] = dp[i]  
            if int(s[i-1:i+1])<27 and int(s[i-1:i+1])>9:
                dp[i+1] += dp[i-1]
        
        return dp[len(s)]