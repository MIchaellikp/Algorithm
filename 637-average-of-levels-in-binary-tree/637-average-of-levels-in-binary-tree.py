# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        
        def helper(n, d):
            
            if n:
                if len(result) == d:
                    result.append([0,0])
                result[d][0] += n.val
                result[d][1] += 1
                
            if n.left:
                helper(n.left, d + 1)
            if n.right:
                helper(n.right, d + 1)
                
              
        helper(root, 0)
        return [ i/c for i,c in result]
                
        
        
        
        
        
        """if not root:
            return [0]
        
        results = []
        
        que = deque([root])
        
        while que:
            size = len(que)
            sum_ = 0
            
            for _ in range(len(que)):
                cur = que.popleft()
                
                sum_ += cur.val
                
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                    
            results.append(sum_ / size)
            
        return results"""