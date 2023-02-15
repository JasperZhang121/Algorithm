class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        n = len(num)-1
        tmp, exp, res = 0 , 0 , []
        
        for i in range(n,-1,-1):
            tmp += 10**exp * num[i]
            exp+=1
            if i == 0:    
                tmp+= k
        
        while tmp!=0:
            res.append(tmp%10)
            tmp = tmp//10
            
        return res[::-1]
    
            
            