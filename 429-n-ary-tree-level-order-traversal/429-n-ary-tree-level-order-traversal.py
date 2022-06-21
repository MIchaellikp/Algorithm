"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        
        def helper(n, d):
            if not n:
                return
            else:
                if len(result) == d:
                    result.append([])
                result[d].append(n.val)
                
                for c in n.children:
                    helper(c, d + 1)
                    
                    
        helper(root, 0)
        
        return result
                
            
                
                