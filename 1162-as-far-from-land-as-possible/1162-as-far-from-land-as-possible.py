class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        m,n,q = len(grid), len(grid[0]),[]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]==1:
                    q.append((r,c,0))   # put all 1 in the queue

        if len(q) == m*n or len(q)==0:
            return -1                   # if no 1 or all 1, return -1
        
        directions,mx = [(0,1),(1,0),(0,-1),(-1,0)],1
        
        while q:
            r,c,d = q.pop(0)
            for dirs in directions:
                dr,dc = dirs
                nr,nc = r+dr,c+dc
                if 0<=nr<m and 0<=nc<m and grid[nr][nc]==0:
                    q.append((nr,nc,d+1))
                    grid[nr][nc] = d+1
                    mx = max(mx,d+1)
        return mx
        
            
        
        
        