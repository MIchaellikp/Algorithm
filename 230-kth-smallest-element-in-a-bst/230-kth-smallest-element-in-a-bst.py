# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        
        arr=[]
        
        def iot(r):
            if r and len(arr)<k:
                if r.left:  iot(r.left)
                arr.append(r.val)
                if r.right: iot(r.right)
        
        iot(root)
        return arr[k-1]