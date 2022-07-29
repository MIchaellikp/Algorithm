# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        dummyHead.next = head
        
        while head and head.next:
            if head.val > head.next.val:
                insertN = head.next
                startN = dummyHead
                while startN.next.val < insertN.val:
                    startN = startN.next
                    
                head.next = insertN.next
                insertN.next = startN.next
                startN.next = insertN
            else:
                head = head.next
                
                
        return dummyHead.next
                