class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        m,q,visit = len(board),deque(),set()
        board.reverse()
        def intToPos(square):
            r = (square-1)//m
            c = (square-1)%m
            if r%2:
                c = m-1-c
            return [r,c]
        
        q.append([1,0]) #[square, moves]
        
        while q:
            square,moves = q.popleft()
            
            for i in range(1,7):
                nextSquare = square+i
                r,c = intToPos(nextSquare)
                
                if board[r][c] != -1:
                    nextSquare= board[r][c]
                if nextSquare == m*m: return moves+1
                
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append([nextSquare,moves+1])
        
        return -1
        

        
        