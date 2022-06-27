# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur_m = -float("INF")
        
        def helper(node):
            nonlocal cur_m
            if not node:
                return True
            
            a = helper(node.left)
            
            if cur_m < node.val:
                self_max = node.val
            else:
                return False
            
            b = helper(node.right)
            
            return a and b
        
        return helper(root)"""

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 规律: BST的中序遍历节点数值是从小到大. 
        cur_max = -float("INF")
        def __isValidBST(node: TreeNode) -> bool: 
            nonlocal cur_max
            
            if not node: 
                return True
            
            is_left_valid = __isValidBST(node.left)
            if cur_max < node.val: 
                cur_max = node.val
            else: 
                return False
            is_right_valid = __isValidBST(node.right)
            
            return is_left_valid and is_right_valid
        return __isValidBST(root)
            