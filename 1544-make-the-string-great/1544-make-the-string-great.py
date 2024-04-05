class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        
        for x in s:
            stack.append(x)
            if len(stack)>=2:
                if stack[-1]!=stack[-2]:
                    if stack[-1].upper()==stack[-2] or stack[-1].lower()==stack[-2]:
                        stack.pop()
                        stack.pop()
        
        res = "".join(stack)
        
        return res