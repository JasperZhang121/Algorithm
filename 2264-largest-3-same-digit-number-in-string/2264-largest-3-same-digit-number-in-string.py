class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        good = []
        
        for i in range(0,len(num)-2):
            if num[i]==num[i+1] and num[i+1]==num[i+2]:
                good.append(num[i:i+3])
        
        if len(good)==1:
            return good[-1]
        elif len(good)==0:
            return ""
        else:
            res = sorted(good)
            return res[-1]