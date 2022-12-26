class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        res = 0
        
        ar = [0]*a
        arr = [0]*b
        
        if ar == []: 
            ar = [0]*(-a)
            res-=len(ar)
        else:
            res+=len(ar)
            
        if arr == []: 
            arr = [0]*(-b)
            res-=len(arr)
        else:
            res+=len(arr)
        return res