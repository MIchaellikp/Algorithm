# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.result = [0]
        self.de = -1
        def helper(node, d):
            if not node.left and not node.right:
                if d > self.de:
                    self.de = d
                    self.result = node.val
                    
            if node.left:
                helper(node.left, d + 1)
                
            if node.right:
                helper(node.right, d + 1)
                
                
        helper(root,0)
        
        return self.result
                    