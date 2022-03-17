"""
March Leetcoding Challenge Day 16
946. Validate Stack Sequences
[Solution]
Language: Python
Time Complexity: O(n)
Space Complexity: O(n) 
"""
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        index = 0
        stack = []
        i = 0
        while i < len(pushed):
            num = pushed[i]
            if num == popped[index]:
                index += 1
                i += 1
            else:
                if len(stack) == 0:
                    stack.append(num)
                    i += 1
                    continue
                pop = stack.pop()
                if pop != popped[index]:
                    stack.append(pop)
                    stack.append(num)
                    i += 1
                else:
                    index += 1
        
        while len(stack):
            num = stack.pop()
            if num != popped[index]:
                return False
            index += 1
            
        return True