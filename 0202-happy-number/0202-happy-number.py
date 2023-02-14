class Solution:
    def isHappy(self, n: int) -> bool:
        
        has = set(); has.add(n)
        
        while n!=1:
            tmp = 0
            while n!=0:
                a = n%10 ; n=n//10
                tmp+=a**2
                
            n = tmp
            
            if n in has:
                return False
            else:
                has.add(n)
        return True
        
        
        
        
        