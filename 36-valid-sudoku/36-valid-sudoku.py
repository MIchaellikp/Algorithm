class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        rowset = [set() for _ in range(len(board))]
        colset = [set() for _ in range(len(board))]
        squset = [set() for _ in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                a = board[i][j]
                if a in rowset[i] or a in colset[j] or a in squset[(i//3) * 3+j//3]:
                    return False
                
                rowset[i].add(a)
                colset[j].add(a)
                squset[(i//3) * 3+j//3].add(a)
                
        return True
                    