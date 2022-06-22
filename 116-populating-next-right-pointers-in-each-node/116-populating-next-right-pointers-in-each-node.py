"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        
        stack = [root]
        result = []
        
        
        while stack:
            n = len(stack)
            for i in range(n):
                cur = stack.pop(0)
                
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                result.append(cur.val)

                if i == n - 1:
                    cur.next = None
                else:
                    cur.next = stack[0]
                    

                
            
        return root