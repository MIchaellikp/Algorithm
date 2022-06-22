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
        

        stack = [root]
        result = []
        
        while stack:
            curr = stack.pop()
            if curr:
                result.append(curr.val)
                for c in curr.children[::-1]:
                    stack.append(c)
        return result