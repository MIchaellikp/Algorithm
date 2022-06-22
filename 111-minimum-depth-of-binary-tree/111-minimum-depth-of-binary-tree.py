# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        md = 0
        
        def helper(r):
            if not r:
                return 0
            return min(helper(r.left), helper(r.right)) + 1
            
        md = helper(root)
        return md"""
    
    
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        #根节点的深度为1
        queue_ = [(root,1)]
        while queue_:
            cur, depth = queue_.pop(0)
            
            if cur.left == None and cur.right == None:
                return depth
            #先左子节点，由于左子节点没有孩子，则就是这一层了
            if cur.left:
                queue_.append((cur.left,depth + 1))
            if cur.right:
                queue_.append((cur.right,depth + 1))

        return 0