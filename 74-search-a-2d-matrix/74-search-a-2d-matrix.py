# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix or not matrix[0]:
#             return False

#         l, r = 0, len(matrix)*len(matrix[0])

#         while l<r:
#             mid = (l+r)//2
#             i, j = mid//len(matrix[0]), mid%len(matrix[0])
#             if matrix[i][j]==target:
#                 return True
#             elif matrix[i][j]>target:
#                 r = mid
#             else:
#                 l = mid + 1
    
#         return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = len(matrix)-1, 0

        while 0<=row<len(matrix) and 0<=col<len(matrix[0]):
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    col += 1
                else:
                    row -= 1
                    
        return False