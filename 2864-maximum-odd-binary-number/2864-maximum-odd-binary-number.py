from collections import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        res = ""
        ones = s.count('1')
        zeros = s.count('0')
        
        if ones == 1:
            res = '0'*zeros+'1'
        else:
            res = '1'*(ones-1)+'0'*zeros+'1'
        
        return res
            