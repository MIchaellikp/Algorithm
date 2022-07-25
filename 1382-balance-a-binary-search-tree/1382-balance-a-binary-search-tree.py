# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        #cover it to a sorted list
        temp = []
        def traversal(r):
            if not r:
                return 
            
            traversal(r.left)
            temp.append(r.val)
            traversal(r.right)
            
        def buildTree(li,l, r):
            if l > r:
                return
            
            m = (l + r) // 2
            root = TreeNode(li[m])
            root.left = buildTree(li,l, m - 1)
            root.right = buildTree(li, m+1, r)
            return root
        
        traversal(root)
        return buildTree(temp,0,len(temp)-1)