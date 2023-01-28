class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        g, v = defaultdict(), set()
        for i in range(len(rooms)):
            g[i] = rooms[i]
            
        
        def dfs(node,count=set(),visited=set()):
            temp = False
            if len(count) == len(rooms):
                return True
            for x in g[node]:
                if x not in visited:
                    count.add(x)
                    visited.add(x)
                    temp = temp or dfs(x,count)
            return temp
        
        count = set([0])
        v = set([0])
        
        return dfs(0,count,v)
            