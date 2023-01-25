class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(r, c) :
            if grid[r][c] == 1 :
                q.append((r, c, 0))
                grid[r][c] = '$'
                if r-1 >= 0 : dfs(r-1, c)
                if r+1 < len(grid) : dfs(r+1, c)
                if c-1 >= 0 : dfs(r, c-1)
                if c+1 < len(grid) : dfs(r, c+1)
        
        def bfs(q) :
            seen = set()
            while q :
                i, j, d = q.popleft()
                if grid[i][j] == 1 :
                    return d
                else :
                    for x, y in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)) :
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) : 
                            if (x, y) not in seen :
                                seen.add((x, y))
                                q.append((x, y, d+1))
        
        q = deque()
        flag = False
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 :
                    dfs(i, j)
                    flag = True
                    break
            if flag :
                break
        
        return bfs(q) - 1               
        
        
        