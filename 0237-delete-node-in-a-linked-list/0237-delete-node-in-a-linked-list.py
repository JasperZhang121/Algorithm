# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        temp = node
        arr = []
        while temp != None:
            arr.append(temp.val)
            temp = temp.next
        
        arr.remove(node.val)
        arr.append(0)
         
        tt = node
        i = 0
        while tt != None:
            tt.val = arr[i]
            tt = tt.next
            i+=1
        
        i-=1
        ttt = node
        while i!=0:
            if i==1:
                ttt.next = None
                break
            else:
                ttt = ttt.next
            i-=1
        
            
        