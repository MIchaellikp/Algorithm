# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        if not root:
            return []
        self.targetSum = targetSum
        self.result = []
        def helper(node, res):
            if not node.left and not node.right:
                if sum(res) == self.targetSum:
                    self.result.append(res[:])
                return

            if node.left:
                res.append(node.left.val)
                
                helper(node.left,res)
                res.pop()
            if node.right:
                res.append(node.right.val)
                helper(node.right,res)
                res.pop()
            

        helper(root,[root.val])
        return self.result"""
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def helper(root, targetSum, currentList, remain):
            if root is None:
                return 
            remain -= root.val
            currentList.append(root.val)
            if root.left is None and root.right is None:
                if remain == 0:
                    result.append(list(currentList))
            helper(root.left, targetSum, currentList, remain)
            helper(root.right, targetSum, currentList, remain)
            currentList.pop()
            
        helper(root, targetSum, [], targetSum)
        return result