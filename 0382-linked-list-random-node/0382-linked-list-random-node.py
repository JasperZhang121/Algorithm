# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.lis = []
        
        while head:    
            self.lis.append(head.val)
            head = head.next
        
    def getRandom(self) -> int:
        a = self.lis
        num = random.randint(0,len(self.lis)-1)
        return self.lis[num]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()