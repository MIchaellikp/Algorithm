# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def help(r,p):
            nonlocal res
            if root:
                p = 10 *p + r.val
                if not r.left and not r.right:
                    res += p
                    return 
            
            if r.left:
                help(r.left, p)
            
            if r.right:
                help(r.right, p)
                
                
            
                
        help(root,0)
        
        return(res)