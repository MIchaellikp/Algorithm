# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur_m = -float("INF")
        
        def helper(node):
            nonlocal cur_m
            if not node:
                return True
            
            a = helper(node.left)
            
            if cur_m < node.val:
                cur_m = node.val
            else:
                return False
            
            b = helper(node.right)
            
            return a and b
        
        return helper(root)
            