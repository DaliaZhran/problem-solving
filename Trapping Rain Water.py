# https://leetcode.com/problems/trapping-rain-water/

"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

# * Approach 1 : Two Pointers
# Idea -> we can see height[left] < height[right],then for pointerleft, he knows a taller bar exists on his right side, then if leftMax is taller than him, he can contain some water for sure(in our case). So we go ans += (left_max - height[left]). But if leftMax is shorter than him, then there isn't a left side bar can help him contain water, then he will become other bars' leftMax. so execute (left_max = height[left]). Same idea for right part.
# Time : O(N) where N is len(height)
# Space : O(1)
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


# check https://leetcode.com/problems/trapping-rain-water-ii