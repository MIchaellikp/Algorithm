"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        def helper(r):
            
            if not r:
                return 
            
            for i in r.children:
                helper(i)
                
            result.append(r.val)
            
        helper(root)
        return result