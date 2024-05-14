class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        maxt = 0
        
        def dfs(x,y,t):
            if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]):
                return 
            
            nonlocal maxt
            
            if grid[x][y]:
                
                t+=grid[x][y]
                temp = grid[x][y]
                grid[x][y] = 0 
                maxt = max(t,maxt)

                for i, j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    dfs(i,j,t)

                grid[x][y]=temp
        
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                dfs(m,n,0)
        return maxt
            
