"""
March Leetcoding Challenge Day 22
1663. Smallest String With A Given Numeric Value
[Solution]
Language: Python
Time Complexity: O(n)
Space Complexity: O(n) <- The output itself is O(n)
"""
class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = []
        while n > 0:
            q = k // 26
            if k % 26 == 0:
                q -= 1
            if q < n - 1:
                ans.append('a')
                n -= 1
                k -= 1
            else:
                if k % 26 == 0:
                    ans.append('z')
                    k -= 26
                    n -= 1
                    continue
                c = chr(k % 26 + ord('a') - 1)
                ans.append(c)
                k -= k % 26
                n -= 1
        
        return ''.join(ans)