/*
March Leetcoding Challenge Day 11
138. Copy List with Random Pointer
[Solution]
Language: C++
Time Complexity: O(n)
Space Complexity: O(n) <- The output itself is O(n)
*/

// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*, Node*> nodeMap;
        Node* curr = head;
        while (curr) {
            nodeMap[curr] = new Node(curr->val);
            curr = curr->next;
        }
        curr = head;
        Node* headCopy = nodeMap[head];
        Node* currCopy = headCopy;
        while (curr) {
            currCopy->next = nodeMap[curr->next];
            currCopy->random = nodeMap[curr->random];
            curr = curr->next;
            currCopy = currCopy->next;
        }
        return headCopy;
    }
};