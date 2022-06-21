# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def helper(n, d):
            if n:
                if len(result) == d:
                    result.append(n.val)
                result[d] = max(result[d], n.val)
                
                if n.left:
                    helper(n.left, d + 1)
                if n.right:
                    helper(n.right, d + 1)
                
        helper(root, 0)
        
        return result
                
            