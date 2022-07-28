# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        
        current = head
        length = 1
        while current.next:
            current = current.next
            length += 1
            
        k = k % length
        
        if k == 0:
            return head
        
        current.next = head

        
        temp = head
        
        for _ in range( length - k - 1):
            temp = temp.next
            
        answer = temp.next
        temp.next = None
        
        return answer