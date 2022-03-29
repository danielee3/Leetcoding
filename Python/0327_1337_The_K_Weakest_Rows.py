"""
March Leetcoding Challenge Day 27
1337. The K Weakest Rows in a Matrix
[Solution]
Language: Python
Time Complexity: O(n^2)
Space Complexity: O(n) <- The output itself is O(n)
"""
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        lst = []
        for row in mat:
            lst.append(sum(row))
        ans = []
        
        while k > 0:
            minVal = 101
            minIndex = -1
            for i in range(len(lst)):
                if lst[i] < minVal:
                    minVal = lst[i]
                    minIndex = i
            lst[minIndex] = 100
            ans.append(minIndex)
            k -= 1
        
        return ans