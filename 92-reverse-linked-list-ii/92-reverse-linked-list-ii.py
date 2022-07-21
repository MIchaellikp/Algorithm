# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        
        for i in range(left-1):
            pre = pre.next
        
        cur = pre.next
        temp = None
        for i in range(left, right+1):
            next = cur.next
            cur.next = temp
            temp = cur
            cur = next
        

        pre.next.next = cur

        pre.next = temp

        
        return dummy.next
        
        
        
        