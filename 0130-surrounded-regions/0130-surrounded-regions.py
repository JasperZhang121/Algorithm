class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == None:
                return 
        m, n = len(board), len(board[0])
        stack = []  
        for i in range(m):
            if board[i][0]=='O':
                stack.append((i,0))
            if board[i][n-1]=='O':
                stack.append((i,n-1))
        
        for i in range(1,n-1):
            if board[0][i]=='O':
                stack.append((0,i))
            if board[m-1][i]=='O':
                stack.append((m-1,i))
                
        while stack:
            i,j = stack.pop()
            if 0<=i<m and 0<=j<n and board[i][j]=='O': 
                board[i][j] = '#'
                stack += (i,j-1),(i,j+1),(i-1,j),(i+1,j)
        board [:] = [['XO'[c=='#']for c in row] for row in board]
        
            