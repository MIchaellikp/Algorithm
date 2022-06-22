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
    def connect(self, root: 'Node') -> 'Node':
        """if not root:
            return None
        
        first = root
        
        while first:
            cur = first
            dummyhead = Node(None) #fake head for next level
            
            start = dummyhead # 
            while cur:
                if cur.left:
                    start.next = cur.left
                    start = start.next
                if cur.right:
                    start.next = cur.right
                    start = start.next
                cur = cur.next
            first = dummyhead.next
        return root"""
        
        if not root:
            return None
        
        stack = [root]
        
        while stack:
            n = len(stack)
            tail = None
            for i in range(n):
                c = stack.pop(0)
                if tail:
                    tail.next = c
                tail = c
                if c.left : stack.append(c.left)
                if c.right: stack.append(c.right)
                    
        return root