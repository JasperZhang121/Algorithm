class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # backtracking  
        # during process, if numbers of RBRA > LBRA, invalid, step out 
        # append in ans when len(S) is max
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans