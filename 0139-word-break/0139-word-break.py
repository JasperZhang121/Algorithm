class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n=len(s)
        dp = [False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            for word in wordDict:
                l = len(word)
                if i>=l and s[i-l:i]==word:
                    if dp[i-l] is True:
                        dp[i] = True
        return dp[n]


