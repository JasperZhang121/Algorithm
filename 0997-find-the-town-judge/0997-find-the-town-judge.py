class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if not trust and n==1:
            return n
        
        mapp = collections.defaultdict(list)
        values = set()
        
        for x,y in trust:
            mapp[y].append(x)
            values.add(x)
            
        for x,y in mapp.items():
            if x not in values and len(y) == n-1:
                return x
        return -1
    