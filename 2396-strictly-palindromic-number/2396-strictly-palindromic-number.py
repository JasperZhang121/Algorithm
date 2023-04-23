class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        for i in range(2,n-1):
            s=self.convert(n,i)
            if str(s)!=str(s)[::-1]:
                return False
        return True

    def convert(self, n,x):
        tem=""
        while n>1:
            tem+=str(n%x)
            if n//x in range(0,x):
                tem+=str(n//x)
            n//=x
        return tem