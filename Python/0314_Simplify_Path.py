"""
March Leetcoding Challenge Day 14 (Pie Day!)
71. Simplify Path
[Solution]
Language: Python
Time Complexity: O(n)
Space Complexity: O(n) <- The output itself is O(n)
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        can_path = []        
        for sub_path in path.split('/'):
            if sub_path == "" or sub_path == ".":
                continue
            if sub_path == '..':
                if len(can_path) > 0:
                    can_path.pop()
                    can_path.pop()
            else:
                can_path.append('/')
                can_path.append(sub_path)
        if len(can_path) == 0:
            can_path.append('/')
        return ''.join(can_path)