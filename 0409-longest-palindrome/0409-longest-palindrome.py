class Solution:
    def longestPalindrome(self, s: str) -> int:
        oddFlag=0
        
        count=collections.Counter(s)

        ans=0
        for k,v in count.items():
            if v%2==1:
                ans+=v-1
                oddFlag= 1
            else:
                ans+=v
                
        if oddFlag == 1:
            return ans+1
        return ans
            
        