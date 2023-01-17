class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = 0
        cntone = 0

        for x in s:
            if x =='1':
                cntone+=1
            else: 
                res = min(res+1,cntone)
        return res
            