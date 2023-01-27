class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        tree = defaultdict(set)
        for u,v in edges:
            tree[u].add(v)
            tree[v].add(u)
        
        seen = {source}
        stack = [source]
        while stack:
            v = stack.pop()
            if v == destination:
                return True
            for u in tree[v]:
                if u not in seen:
                    seen.add(u)
                    stack.append(u)
        return False