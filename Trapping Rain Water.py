# https://leetcode.com/problems/trapping-rain-water/

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

# * Approach 1 : Two Pointers
# Time -> O(N)
# Space -> O(1)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        answer = 0

        while left < right:
            if height[left] >= height[right]:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    answer += rightMax - height[right]
                right -= 1

            else:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    answer += leftMax - height[left]
                left += 1
        return answer


# * Approach 2 : DP
# Time -> O(N)
# Space -> O(N)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] < max_left:
                    water += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1
            else:
                if height[right] < max_right:
                    water += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1

        return water


# check https://leetcode.com/problems/trapping-rain-water-ii