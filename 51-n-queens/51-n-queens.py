"""class Solution:
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
        return res"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #Cannot be same column/row/diag
        #Need to store col/diagonal cells of queens already placed down. Already going to iterate diff rows so don't need to remember that
        #Guaranteed that there are n queens, so one on every row
        
        cols=set()
        posDiag=set()  #n-1 diag is the one from n-1,0 / to top right. > is bottom right of it, < is top left  
        negDiag=set()  #0 diag is the one from 0,0 \ to end. -1 is top right of it, 1 is bottom left
        res=[]
        #Create board
        board=[["."]*n for _ in range(n)]
        
        def backtrack(i):
            #Reached the last row, last queen has been put down
            #If couldnt reach n queens by last row then it'll just pass through the whole method and backtrack without adding

            if i==n:  
                currRes=["".join(row) for row in board]   #Need to join rows to string for answer format
                res.append(currRes)
                return
            
            #Try every column with this row. ONLY update sets and place queen down if valid
            for j in range(n):
                if j not in cols and i+j not in posDiag and i-j not in negDiag:
                    cols.add(j)     #One in this column allowed
                    posDiag.add(i+j)  #One in this diagonal allowed (based on /, all cells in same diag have same ID)
                    negDiag.add(i-j)  #One in this diagonal allowed (based on \, all cells in same diag have same ID)
                    board[i][j]= "Q"
                    
                    #Placed queen and attempting with next row. 
                    #When returning take back this queen and try with next column of this row
                    backtrack(i+1)
                    
                    cols.discard(j)
                    posDiag.discard(i+j)  
                    negDiag.discard(i-j)
                    board[i][j]= "."        
        

        backtrack(0)  #Start with row 0, AKA 0 queens placed down
        return res

