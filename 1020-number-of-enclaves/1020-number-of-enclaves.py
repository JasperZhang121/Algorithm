class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        
        m,n = len(grid), len(grid[0])
        lis = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def dfs(x,y):
            
            if grid[x][y] != 1:
                return
            if grid[x][y] == 1:
                grid[x][y] = 2
                
            for a,b in lis:
                curx = a+x
                cury = b+y
                if 0<=curx<m and 0<=cury<n:
                    dfs(curx,cury)
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i==0 or j==0 or i==m-1 or j==n-1):
                    dfs(i,j)
        
        res = 0   
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    res+=1

        return res       
                    