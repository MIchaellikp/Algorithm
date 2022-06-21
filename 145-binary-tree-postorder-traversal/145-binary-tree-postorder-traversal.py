# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """'''result = []
        
        def traversal(r):
            if r == None:
                return
            
            traversal(r.left)
            traversal(r.right)
            result.append(r.val)
            
            
        traversal(root)
        return result'''"""

        if not root:
            return []
        
        stack = [root]
        result = []

        while stack:
            
            node = stack.pop()
            result.append(node.val)
            
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)
                
        return result[::-1]
            
            