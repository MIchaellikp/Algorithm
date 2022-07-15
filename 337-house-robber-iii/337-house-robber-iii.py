# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memory = {}
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return root.val
        if self.memory.get(root) is not None:
            return self.memory[root]
        
        va1 = root.val
        
        if root.left:
            va1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            va1 += self.rob(root.right.left) + self.rob(root.right.right)
            
        
        val2 = self.rob(root.left) + self.rob(root.right)
        self.memory[root] = max(val2,va1)
        return max(val2, va1)