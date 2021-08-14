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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* a = l1;
        ListNode* b = l2;
        
        if(a == nullptr && b == nullptr) return nullptr;

        ListNode* newList = new ListNode();
        ListNode* t = newList;
        
        while(a != nullptr || b != nullptr) {
            if(a == nullptr) {
                t->val = b->val;
                b = b->next;
            } else if (b == nullptr) {
                t->val = a->val;
                a = a->next;
            } else if(a->val < b->val) {
                t->val = a->val;
                a = a->next;
            } else {
                t->val = b->val;
                b = b->next;
            }
            
            if(a || b) {
                t->next = new ListNode();
                t = t->next;
            }
        }
        
        return newList;
        
    }
};