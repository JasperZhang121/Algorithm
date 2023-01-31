class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        pairs = [[scores[i],ages[i]] for i in range(len(scores))]
        pairs.sort()
        dp = [pairs[i][0] for i in range(len(pairs))]
        
        
        for i in range(len(pairs)):
            ms, ma = pairs[i]
            for j in range(i):
                s,a = pairs[j]
                if ma>=a:
                    dp[i] = max(dp[i],ms+dp[j])
                
        
        return max(dp)