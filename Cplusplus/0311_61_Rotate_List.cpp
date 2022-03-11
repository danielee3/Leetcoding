/*
March Leetcoding Challenge Day 11
61. Rotate List
[Solution]
Language: C++
Time Complexity: O(n)
Space Complexity: O(n) <- The output itself is O(n)
*/

//  Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) return head;
        int len = 1;
        ListNode* curr = head;
        while (curr->next) {
            len++;            
            curr = curr->next;
        }
        curr->next = head;
        k %= len;
        k = len - k;
        while (k > 0) {
            k--;
            curr = curr->next;
        }
        ListNode* ans = curr->next;
        curr->next = nullptr;
        return ans;
    }
};