# https://leetcode.com/problems/container-with-most-water/

"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

"""

# * Approach 1: Brute Force
# time: O(n^2)
# space: O(1)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = -1
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area


# * Approach 2: Sliding Window
# time: O(n)
# space: O(1)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxProduct = -1

        while left < right:
            product = (right - left) * min(height[left], height[right])
            maxProduct = max(product, maxProduct)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxProduct


# [1,8,6,2,5,4,8,3,7]
