# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dum = ListNode(0)
        dum.next = head
        l, first = 0, head
        
        while first != None:
            l+=1
            first = first.next
        l-=n
        first = dum
        while l>0:
            l-=1
            first = first.next
            
        first.next = first.next.next
        return dum.next
        
        