# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        
        while cur:
            if cur.left:
                r = cur.left
                while r.right:
                    r = r.right
                r.right, cur.right, cur.left = cur.right, cur.left, None
            cur = cur.right