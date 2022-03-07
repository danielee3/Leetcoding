"""
March Leetcoding Challenge Day 7
21. Merge Two Sorted Lists
[Solution]
Language: Python
Time Complexity: O(n)
Space Complexity: O(n)
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        point1 = list1
        point2 = list2
        val = point1.val
        if point1.val > point2.val:
            val = point2.val
            point2 = point2.next
        else:
            point1 = point1.next
        head = ListNode(val)
        curr = head
        while point1 is not None and point2 is not None:
            if point1.val > point2.val:
                next_node = ListNode(point2.val)
                curr.next = next_node
                curr = curr.next
                point2 = point2.next
            else:
                next_node = ListNode(point1.val)
                curr.next = next_node
                curr = curr.next
                point1 = point1.next
        if point1 is None:
            curr.next = point2
        else:
            curr.next = point1
        return head