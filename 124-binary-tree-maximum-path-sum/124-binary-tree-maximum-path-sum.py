# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         res = float('-inf')
        
#         def helper(n):
#             nonlocal res
#             if not n:
#                 return 0
            
#             l = max(helper(n.left), 0)
#             r = max(helper(n.right), 0)
            
#             c = n.val + l + r
#             res = max(c, res)
            
#             return c + max(l, r)
            
#         helper(root)
        
#         return res
    
    
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf") # placeholder to be updated
        def get_max_gain(node):
            nonlocal max_path # This tells that max_path is not a local variable
            if node is None:
                return 0
            gain_on_left = max(get_max_gain(node.left), 0) # Read the part important observation
            gain_on_right = max(get_max_gain(node.right), 0)  # Read the part important observations
		
            current_max_path = node.val + gain_on_left + gain_on_right
            max_path = max(max_path, current_max_path) # Read first three images of going down the recursion stack
            return node.val + max(gain_on_left, gain_on_right) 
        
        get_max_gain(root)
        return max_path
            