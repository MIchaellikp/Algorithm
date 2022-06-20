# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        def tr(r):
            
            if r == None:
                return
            
            tr(r.left)
            result.append(r.val)
            tr(r.right)
            
            
        tr(root)
        
        return result