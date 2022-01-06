# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def recurse(cn):
            if not cn:
                return False
            
            left = recurse(cn.left)
            
            right = recurse(cn.right)
            
            mid =  cn == p or cn == q
            
            if left + right + mid >= 2:
                self.ans =  cn
            
            return left or right or mid
        
        
        recurse(root)
        
        return self.ans
    
    
    
