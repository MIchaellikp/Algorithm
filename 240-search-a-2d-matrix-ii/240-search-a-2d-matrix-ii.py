class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not len(matrix) or not len(matrix[0]):
            # Quick response for empty matrix
            return False
        n = len(matrix)
        w = len(matrix[0])
        
        
        for row in matrix:
            if row[0] <= target:
                if row[0] <= target <= row[-1]:
                    l, r = 0, w - 1
                    while l <= r:
                        m = l + (r - l) // 2

                        if row[m] > target:
                            r = m - 1
                        elif row[m] < target:
                            l = m + 1
                        else:
                            return True
            else:
                return False


        return False