class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        
        m,n,res = len(grid), len(grid[0]),0
        
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return False
            
            if grid[i][j] == 1:
                return True
            
            grid[i][j] = 1 
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            return left and right and up and down
                         
    
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and dfs(i,j):
                        res+=1
         
        return res