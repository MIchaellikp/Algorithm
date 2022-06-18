# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        
        def dfs(ro):
            if not ro:
                return 'covered'
            
            l = dfs(ro.left)
            r = dfs(ro.right)
            
            if l == 'covered' and  r == 'covered':
                return 'to_be_covered'
            if l == 'to_be_covered' or  r == 'to_be_covered':
                self.count += 1
                return 'coverning'
            if l == 'coverning' or r == 'coverning':
                return 'covered'
            
        
        return (dfs(root) == 'to_be_covered') + self.count