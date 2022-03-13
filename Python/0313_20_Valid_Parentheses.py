"""
March Leetcoding Challenge Day 13
20. Valid Parentheses
[Solution]
Language: Python
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                pop = stack.pop()
                if pop == '(' and c == ')':
                    continue
                elif pop == '{' and c == '}':
                    continue
                elif pop == '[' and c == ']':
                    continue
                else:
                    return False
        return len(stack)==0