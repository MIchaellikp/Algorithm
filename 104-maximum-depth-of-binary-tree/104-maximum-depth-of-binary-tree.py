# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        queue_ = [root]
        result = []
        while queue_:
            length = len(queue_)
            sub = []
            for i in range(length):
                cur = queue_.pop(0)
                sub.append(cur.val)
                #子节点入队列
                if cur.left: queue_.append(cur.left)
                if cur.right: queue_.append(cur.right)
            result.append(sub)
            

        return len(result)
        