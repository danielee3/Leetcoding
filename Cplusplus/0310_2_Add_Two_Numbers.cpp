/*
March Leetcoding Challenge Day 10
2. Add Two Numbers
[Solution]
Language: C++
Time Complexity: O(n)
Space Complexity: O(n) <- The output itself is O(n)
*/

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* curr = head;
        int carry;
        while (l1 != nullptr || l2 != nullptr) {
            carry = curr->val / 10;
            curr->val = curr->val % 10;
            int newVal = (l1==nullptr)?0:l1->val;
            newVal += (l2==nullptr)?0:l2->val;
            curr->next = new ListNode(newVal + carry);
            curr = curr->next;
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }
        carry = curr->val / 10;
        curr->val = curr->val % 10;
        if (carry) curr->next = new ListNode(carry);
        return head->next;
    }
};