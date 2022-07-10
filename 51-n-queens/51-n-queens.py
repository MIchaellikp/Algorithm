class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if not n:
            return n
        board = [["."] * n for _ in range(n)]
        res = []
        def isvalid(r,c):
            
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
                
            i = r - 1
            j = c - 1
            
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
                
            i = r - 1
            j = c + 1
            
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
                
            return True
        
        def backtrack(board, row, n):
            if row == n:
                temp = []
                for i in board:
                    i_star = ''.join(i)
                    temp.append(i_star)
                    
                res.append(temp)
            
            for c in range(n):
                if not isvalid(row, c):
                    continue
                board[row][c] = 'Q'
                backtrack(board, row + 1, n)
                board[row][c] = '.'
                
        backtrack(board, 0,n)
        return res