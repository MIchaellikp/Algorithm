class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        next_row = triangle[-1][:]
        current_row = [0] * n
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                current_row[j] = triangle[i][j] + min(next_row[j] , next_row[j+1])
            current_row, next_row = next_row, current_row
            
        return next_row[0]