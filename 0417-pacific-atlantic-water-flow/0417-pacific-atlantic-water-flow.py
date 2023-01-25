class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        M, N = len(heights), len(heights[0])
        visitedP=set()
        visitedA=set()
        
        def dfs(i, j, preHeight, visited):            
            if 0<=i<M and 0<=j<N and heights[i][j]>=preHeight and (i,j) not in visited:
                visited.add((i,j))
                dfs(i-1, j, heights[i][j], visited)
                dfs(i+1, j, heights[i][j], visited)
                dfs(i, j-1, heights[i][j], visited)
                dfs(i, j+1, heights[i][j], visited)
            
        for j in range(N):
            dfs(0, j, heights[0][j], visitedP)
            dfs(M-1, j, heights[M-1][j], visitedA)
            
        for i in range(M):
            dfs(i, 0, heights[i][0], visitedP)
            dfs(i, N-1, heights[i][N-1], visitedA)
        
        return list(visitedP & visitedA)        