# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        t1 = l1
        t2 = l2
        carry = 0
        
        while t1!=None and t2!= None:
            
            temp = t1.val + t2.val +carry
            t1.val = temp
            t2.val = temp
            
            if carry==1:
                carry=0
            
            if temp>=10:
                t1.val = temp%10
                t2.val = temp%10    
                carry+=1
            t1t = t1
            t2t = t2
            t1=t1.next
            t2=t2.next
            
        
        if t1==None and t2!=None and carry==1:
            while t2!=None:
                
                if carry == 0:
                    break
                else:
                    temp = t2.val+carry
                    if temp>=10:
                        t2.val = temp%10
                        carry =1
                    else:
                        t2.val = temp
                        carry =0
                t2t = t2
                t2=t2.next
                
            if carry ==1:
                tem = ListNode(1)
                t2t.next = tem
            return l2
                
        elif t2==None and t1!=None and carry==1:
            while t1!=None:
                
                if carry == 0:
                    break
                else:
                    temp = t1.val+carry
                    if temp>=10:
                        t1.val = temp%10
                        carry =1
                    else:
                        t1.val = temp
                        carry =0
                t1t=t1
                t1=t1.next
            if carry ==1:
                tem = ListNode(1)
                t1t.next = tem
            return l1
        
        elif t1==None and t2==None and carry ==1:
                tem = ListNode(1)
                t1t.next = tem
                return l1
            
        else:
            if t1!=None:
                return l1
            else:
                return l2
        
            
        
            
