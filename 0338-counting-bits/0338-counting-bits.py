class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = [0]*(n+1)
        
        for i in range(0,n+1):
            bina = bin(i).count('1')
            res[i] = bina
        return res
            