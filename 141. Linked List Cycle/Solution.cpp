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
    bool hasCycle(ListNode *head) {
        vector<ListNode*> addrs;
        
        while (head != NULL){
            for (ListNode* addr: addrs){
                if (head == addr){
                    return true;
                }
            }
            addrs.push_back(head);
            head = head->next;
        }

        return false;
    }
};