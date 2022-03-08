"""
March Leetcoding Challenge Day 8
141. Linked List Cycle
[Solution]
Language: Python
Time Complexity: O(n)
Space Complexity: O(1)
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        if head.next is None:
            return False
        pointer = head
        while pointer and pointer.next:
            pointer = pointer.next.next
            head = head.next
            if head is pointer:
                return True
        return False