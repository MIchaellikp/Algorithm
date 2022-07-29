# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return 
        if not head.next:
            return TreeNode(head.val)
        
        fast, slow = head.next.next, head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
            
        temp = slow.next
        res = ListNode(temp.val)
        slow.next = None
        res.right = self.sortedListToBST(temp.next)
        res.left = self.sortedListToBST(head)
        
        return res