"""
March Leetcoding Challenge Day 17
856. Score of Parentheses
[Solution]
Language: Python
Time Complexity: O(n)
Space Complexity: O(n) 
"""
class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        for p in s:
            if p == '(':
                stack.append(0)
            else:
                stack.append(max(2 * stack.pop(), 1) + stack.pop())
        return stack.pop()