# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def s(r):
            if not r:
                return False
            a = False
            if r.val == subRoot.val:
                a =  isSametree(r,subRoot)
            if a:
                return a
            else:
                return s(r.left) or s(r.right)
        
        
        
        def isSametree(r, s):
            if r is None and s is None:
                return True
            elif r is None or s is None:
                return False
            else:
                if r.val == s.val:
                    return isSametree(r.left, s.left) and isSametree(r.right, s.right)
                else:
                    return False
        
        if not root and not subRoot:
            return True
        elif not root:
            return Flase
        
        return s(root)
        
