/*
March Leetcoding Challenge Day 9
82. Remove Duplicates from Sorted List II
[Solution]
Language: C++
Time Complexity: O(n)
Space Complexity: O(1)
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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) return head;
        ListNode* newHead = new ListNode();
        ListNode* curr = newHead;
        int val;
        while (head != nullptr) {
            val = head->val;
            if (head->next != nullptr && val == head->next->val) {
                while (val == head->val) {
                    if (head->next == nullptr) {
                        curr->next = nullptr;
                        return newHead->next;
                    }
                    head = head->next;
                }
            } else {
                curr->next = head;
                curr = head;
                head = head->next;
            }
        }
        return newHead->next;
    }
};