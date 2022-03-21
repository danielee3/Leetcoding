"""
March Leetcoding Challenge Day 21
763. Partition Labels
[Solution]
Language: Python
Time Complexity: O(n)
Space Complexity: O(1) 
"""
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i
        ans = []
        cut = 0 #The most recent cut made
        max_last = 0 #The maximum of all last indices of characters appeared so far
        for i, c in enumerate(s):
            max_last = max(max_last, last_index[c])
            if i == max_last:
                ans.append(i+1-cut)
                cut = i+1
        return ans