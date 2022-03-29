"""
March Leetcoding Challenge Day 26
704. Binary Search
[Solution]
Language: Python
Time Complexity: O(log n)
Space Complexity: O(1)
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mn = 0
        mx = len(nums) - 1
        index = mn + ((mx-mn)/2)
        while mn <= mx:
            if target == nums[index]:
                return index
            elif target < nums[index]:
                mx = index-1
            else:
                mn = index+1
            index = mn + ((mx-mn)/2)
        return -1