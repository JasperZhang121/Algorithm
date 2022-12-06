class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    for a in range(m):
                        if matrix[a][j]== 0:
                            continue
                        else:
                            matrix[a][j]= 9999999
                    for b in range(n):
                        if matrix[i][b] == 0:
                            continue
                        else:
                            matrix[i][b]= 9999999

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==9999999:
                   matrix[i][j] = 0                 

