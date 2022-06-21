# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        results = []
        
        from collections import deque
        
        que = deque([root])
        
        while que:
            
            node= que[-1]
            results.append(node.val)
            
            result = []
            
            for _ in range(len(que)):
                
                cur = que.popleft()
                #result.append(cur.val)
                
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                    
            #results.append(result[-1])
            
        return results
        
        
        