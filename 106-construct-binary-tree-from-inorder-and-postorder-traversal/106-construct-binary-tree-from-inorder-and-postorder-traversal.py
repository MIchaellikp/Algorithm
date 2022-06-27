# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None
        
        root_val = postorder[-1]
        
        root = TreeNode(root_val)
        
        index = inorder.index(root_val)
        
        inorder_left = inorder[:index]
        inorder_right = inorder[index + 1 :]
        
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder) - 1]
        
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        
        
        return root"""


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        
        def helper(pStart, pEnd, iStart, iEnd):
            if pStart > pEnd:
                return 
            
            rootVal = postorder[pEnd]
            rootIdx = in_map[rootVal]
            leftCnt = rootIdx - iStart
            
            root = TreeNode(rootVal)
            root.left = helper(pStart, pStart+leftCnt-1, iStart, rootIdx-1)
            root.right = helper(pStart+leftCnt, pEnd-1, rootIdx+1, iEnd)
            
            return root
            
        
        in_map = dict()
        for i, x in enumerate(inorder):
            in_map[x] = i
            
        return helper(0, n-1, 0, n-1)