# https://leetcode.com/problems/container-with-most-water/

"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

"""

# O(N)
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
