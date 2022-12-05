class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # row is m
        m = len(matrix)
        
        # n is col
        n = len(matrix[0])
        
        # set boundaries
        up, down = 0, m-1 
        right,left = n-1, 0
        
        # res
        res = []
        
        while True:
            
            # loop top row 
            for i in range(left, right+1, 1):
                res.append(matrix[up][i])
            up+=1
            if up > down: break
            
            # loop right 
            for i in range(up, down+1, 1):
                res.append(matrix[i][right])
            right-=1
            if right<left: break
                
            # loop down
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down-=1
            if up>down: break
            
            # loop left
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left+=1
            if left>right: break
        
        return res
            