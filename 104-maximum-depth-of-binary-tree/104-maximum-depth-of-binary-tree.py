# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        md = 0
        
        def helper(r):
            if not r:
                return 0
            return max(helper(r.left), helper(r.right)) + 1
            
        md = helper(root)
        return md
        