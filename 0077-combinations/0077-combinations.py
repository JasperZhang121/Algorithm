class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        def BT(temp, start):
            if len(temp)==k:
                res.append(temp[:])
                return 
            for x in range(start+1,n+1):
                temp.append(x)
                BT(temp,x)
                temp.pop()
                
        
        BT([],0)
        return res
        
        
        
        
        