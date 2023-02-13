class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(string):
            back,res = 0,''
            string = string[::-1]
            for x in string:
                if x == '#':
                    back+=1
                else:
                    if back>0:
                        back-=1
                    else:
                        res+=x
                    
            return res[::-1]
    
        return helper(s)==helper(t)