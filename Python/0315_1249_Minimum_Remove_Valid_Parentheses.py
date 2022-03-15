"""
March Leetcoding Challenge Day 15
1249. Minimum Remove to Make Valid Parentheses
[Solution]
Language: Python
Time Complexity: O(n)
Space Complexity: O(n) <- The output itself is O(n)
"""
class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        paren = []
        valid = []
        for c in s:
            if c == '(':
                paren.append(c)
            if c == ')':
                if len(paren) == 0:
                    continue
                paren.pop()
            valid.append(c)
        
        if len(paren) == 0:
            return ''.join(valid)
        
        for i in range(len(valid)):
            if len(paren) == 0:
                break
            if valid[len(valid)-1-i] == '(':
                paren.pop()
                valid[len(valid)-1-i] = ''

        return ''.join(valid)