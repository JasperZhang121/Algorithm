class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # backtracking
        
        res = []
        path = []  
        def backtracking():
            if sum(path)>target:
                return
            elif sum(path)==target:
                if path == sorted(path):
                    temp = path.copy()
                    res.append(temp)
                    return
            else:
                for x in candidates:
                    path.append(x)
                    backtracking()
                    path.pop()
        backtracking()
        return res
            