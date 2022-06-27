# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def traverse_tree(tree_node: Optional[TreeNode], current_sum: int):
            if not tree_node:
                return False
            
            is_leaf = (tree_node.left is None and tree_node.right is None)
            if is_leaf:
                # print(f"leaf_sum: {current_sum} with node val: {tree_node.val} = {current_sum + tree_node.val}")
                if (current_sum + tree_node.val) == targetSum:
                    return True
            else:
                # print(f"not leaf: node val: {tree_node.val} leaf_sum: {leaf_sum}")
                current_sum += tree_node.val
                # print(f"after: not leaf: node val: {tree_node.val} current_sum: {current_sum}")
            return traverse_tree(tree_node.left, current_sum) or traverse_tree(tree_node.right, current_sum)
        
        return traverse_tree(root, 0)
                