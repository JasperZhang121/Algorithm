class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c :
            return mat 

        cnt = 0
        ans = []
        row = []
        for i in range(m):
            for j in range(n):
                row.append(mat[i][j])
                cnt+=1
                if cnt == c:
                    ans.append(row)
                    row = []
                    cnt = 0
        return ans