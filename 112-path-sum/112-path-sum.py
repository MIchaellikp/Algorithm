# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root :
            return False
        
        
        self.targetSum = targetSum
        
        def helper(node, val):
            if not node.left and not node.right:
                if val == self.targetSum:
                    return True
                else:
                    return False
                
            if node.left:
                val += node.left.val
                if helper(node.left,val):
                    return True
                val -= node.left.val
            if node.right:
                val += node.right.val
                if helper(node.right,val):
                    return True
                val -= node.right.val
            
            return False
        
        return helper(root,root.val)
                