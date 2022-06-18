# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        cur = dummy
        
        while cur.next and cur.next.next:
            cnext = cur.next
            cnnext = cur.next.next
            
            cnext.next = cnnext.next
            cnnext.next = cnext
            cur.next = cnnext
            
            cur = cur.next.next
            
        return dummy.next