# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        
        """def helper(node):
            if not node:
                return
            
            if node.left and not node.left.left and not node.left.right:
                self.result += node.left.val
                
                
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return self.result"""
        stack = []
        if root: 
            stack.append(root)
        res = 0
        
        while stack: 
            # 每次都把当前节点的左节点加进去. 
            cur_node = stack.pop()
            if cur_node.left and not cur_node.left.left and not cur_node.left.right: 
                res += cur_node.left.val
                
            if cur_node.left: 
                stack.append(cur_node.left)
            if cur_node.right: 
                stack.append(cur_node.right)
                
        return res