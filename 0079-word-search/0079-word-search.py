class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(i,j,word,start,board):
            if start>=len(word):
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False
            if board[i][j]==word[start]:
                start+=1
                c = board[i][j]
                board[i][j] = '#'
                res = helper(i-1,j,word,start,board) or helper(i+1,j,word,start,board) or helper(i,j-1,word,start,board) or helper(i,j+1,word,start,board)
                board[i][j]=c
                return res
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i,j,word,0,board):
                    return True
        return False