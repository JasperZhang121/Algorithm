class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row, col):
            if row < 0 or row >= len(grid):
                return
            
            if col < 0 or col >= len(grid[0]):
                return
            
            if grid[row][col] != '1':
                return
            
            grid[row][col] = 'x'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
            
        ans = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)
        
        return ans
    
