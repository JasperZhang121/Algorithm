/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        
        ListNode *slow = head, *fast = head;
        
        do{
            if (!fast || !fast->next) return nullptr;
            fast = fast->next->next;
            slow = slow->next;
            
        }while(fast!=slow); // when first time meets, put fast at head
        
        fast = head;
        while (fast!=slow){ // when second time meets, meeting point is the start of the loop
            slow = slow->next;
            fast = fast->next;
        }
        return fast;
    }
};