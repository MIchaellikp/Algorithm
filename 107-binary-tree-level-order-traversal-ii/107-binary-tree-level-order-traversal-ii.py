# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """result = []
        
        def helper(r, d):
            if not r:
                return
            
            if len(result) == d:
                result.append([])
                
            result[d].append(r.val)
            
            if r.left: helper( r.left, d + 1)
            if r.right: helper( r.right, d + 1)
            
            
        helper(root, 0)
        result.reverse()
        
        return result"""
        """if not root:
            return []
        results = []
        from collections import deque
        que = deque([root])
        
        while que:
            result = []
            for _ in range(len(que)):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)
            
        results.reverse()"""
        
        if not root:
            return root
        queue = deque([root])
        
        levels = []
        
        while queue:
            
            nodes_length = len(queue)
            levels.append([])
            for i in range(nodes_length):
                node = queue.popleft()
                levels[len(levels)-1].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
        return levels[::-1]