class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        x = len(matrix) - 1
        y = len(matrix[0]) - 1
        startx, starty = 0, 0
        
        while (startx < x and starty < y):
            for i in range(starty, y):
                result.append(matrix[startx][i])
            
            for i in range(startx, x):
                result.append(matrix[i][y])
                
            for i in range(y , starty, -1):
                result.append(matrix[x][i])
                
            for i in range(x, startx, -1):
                result.append(matrix[i][startx])
                
            startx += 1
            starty += 1
            x -= 1
            y -= 1
            

        if len(result) < (len(matrix)) * (len(matrix[0]) ):
            for r in range(startx, x + 1):
                for c in range(starty, y + 1):
                    result.append(matrix[r][c])
                    
        return result 
            
            
            