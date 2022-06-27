# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """if not preorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        separator_index = inorder.index(root_val)
        
        inorder_left = inorder[:separator_index]
        inorder_right = inorder[separator_index + 1:]
        
        preorder_left = preorder[1 : 1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left): ]
        
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        
        return root"""
        
        n = len(preorder)
        
        d = dict()
        
        for i, v in enumerate(inorder):
            d[v] = i
            
        self.preorder_index = 0
        
        def helper(left ,right):
            if left > right:
                return
            
            rootVal = preorder[self.preorder_index]
            self.preorder_index += 1
            in_i = d[rootVal]
            
            root = TreeNode(rootVal)
            
            root.left = helper(left, in_i - 1)
            root.right = helper(1 + in_i, right)
            return root
            
        return helper(0, n - 1)
            
            
            
            
            
            