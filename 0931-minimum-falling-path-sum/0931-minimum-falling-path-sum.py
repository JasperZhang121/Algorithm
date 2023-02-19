class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        m,n = len(matrix),len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                
                if i == 0 :
                    continue
                elif j==0:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j+1])
                elif j==n-1:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1])
                else:
                    matrix[i][j] += min(matrix[i-1][j],matrix[i-1][j-1],matrix[i-1][j+1])
        
        
        return min(matrix[m-1])