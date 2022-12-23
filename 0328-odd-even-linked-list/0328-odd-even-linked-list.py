# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None : return None
            
        odd = head
        dum = evn = head.next
        
        while evn and evn.next:
            odd.next = odd.next.next
            evn.next = evn.next.next
            odd = odd.next
            evn = evn.next
            
        odd.next = dum

        return head 
        