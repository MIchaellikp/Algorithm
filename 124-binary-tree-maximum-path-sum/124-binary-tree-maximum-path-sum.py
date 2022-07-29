# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        
        def helper(n):
            nonlocal res
            if not n:
                return 0
            
            l = max(helper(n.left), 0)
            r = max(helper(n.right), 0)
            
            c = n.val + l + r
            res = max(c, res)
            
            return n.val + max(l, r)
            
        helper(root)
        
        return res
    
