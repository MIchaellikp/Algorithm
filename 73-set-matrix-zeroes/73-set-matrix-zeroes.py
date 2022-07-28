class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c = set()
        r = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    c.add(j)
                    r.add(i)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in r or j in c:
                    matrix[i][j] = 0
        