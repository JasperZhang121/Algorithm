class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(x,y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return 0
            if not grid[x][y]:
                return 0
            if grid[x][y]:
                grid[x][y] = 0
                return 1+dfs(x-1,y)+dfs(x+1,y)+dfs(x,y-1)+dfs(x,y+1)
                    
        m = len(grid)
        n = len(grid[0])
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = max(dfs(i,j), area)
        return area
            
        
            
        
        