class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)-1
        c = 0
        while n>=0:
            if n == len(digits)-1:
                digits[n]+=1
                if digits[n]==10:
                    digits[n]=0
                    c=1
                n-=1
            else:
                digits[n] +=c
                if digits[n]==10:
                    digits[n]=0
                    c=1
                    n-=1
                else:
                    c=0
                    break
            
        if c==1:
            res = [1]
            res.extend(digits)
            return res
        else:
            return digits