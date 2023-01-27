class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def values(exp):
            ans, number = [], 0
            for i in range(len(exp)):
                if not exp[i].isdigit():
                    for l in values(exp[:i]):
                        for r in values(exp[i+1:]):
                            if exp[i]=='+': ans.append(l+r)                           
                            elif exp[i]=='-': ans.append(l-r)
                            elif exp[i]=='*': ans.append(l*r)
                else:number = number * 10 + int(exp[i])
            return ans if ans else [number]     
        return values(expression)