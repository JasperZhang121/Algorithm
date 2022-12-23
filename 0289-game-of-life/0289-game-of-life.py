class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows, cols = len(board),len(board[0])
        
        def couN(r,c):
            n = 0
            for i in range (r-1,r+2):
                for j in range (c-1, c+2):
                    if ((i==r and j==c) or i<0 or j<0 or i == rows or j == cols):
                        continue
                    if board[i][j] in [1,3]:
                        n+=1
            return n
        
        for r in range(rows):
            for c in range(cols):
                n = couN (r,c)
                if board[r][c]:
                    if n in [2,3]:
                        board[r][c] = 3
                elif n == 3:
                        board[r][c] = 2
       
        for r in range (rows):
            for c in range(cols):
                if  board[r][c] == 1:
                    board[r][c]= 0
                elif board[r][c] in [2,3]:
                    board[r][c]= 1
        
        
        
                            
                            
                    
        