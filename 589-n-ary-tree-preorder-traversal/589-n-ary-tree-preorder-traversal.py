"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        """result = []
        
        def helper(r):
            if not r:
                return 
            result.append(r.val)
            for i in r.children:
                helper(i)
                
        helper(root)
        return result"""
        
        if not root:
            return []
        
        queue = [root]
        result = []
        while queue:
            cur = queue.pop()
            result.append(cur.val)
            temp = []
            for i in cur.children:
                temp.append(i)
            queue.extend(temp[::-1])
        
        return result