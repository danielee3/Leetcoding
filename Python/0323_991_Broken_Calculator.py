"""
March Leetcoding Challenge Day 23
991. Broken Calculator
[Solution]
Language: Python
Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        count = 0
        while target > startValue:
            if target % 2 == 1:
                count += 1
                target += 1
            else:
                count += 1
                target /= 2
        count +=  startValue - target
        return count