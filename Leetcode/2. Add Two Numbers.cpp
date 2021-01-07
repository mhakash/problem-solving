/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* t1 = l1;
        ListNode* t2 = l2;
        
        int s = l1->val + l2->val;
        int r = s/10;
        ListNode* l = new ListNode(s%10);
        ListNode* x = l;

        t1 = t1->next;
        t2 = t2->next;
        
        while(t1 || t2 || r){
            if(!t1) t1 = new ListNode();
            if(!t2) t2 = new ListNode();
            
            s = t1->val + t2->val + r;
            ListNode* temp = new ListNode(s%10);
            r = s/10;
            x->next = temp;
            x = x->next;
            
            t1 = t1->next;
            t2 = t2->next;
        }
        return l;
    }
};