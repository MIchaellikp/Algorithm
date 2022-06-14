class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        result = triangle
        if len(triangle) == 1:
            return triangle[0][0]
        
        print(result)
        for i in range(len(result) - 2, -1, -1):
            for j in range(len(triangle[i])):
                result[i][j] = triangle[i][j] + min(triangle[i+1][j] , triangle[i+1][j+1])
            
        return result[0][0]