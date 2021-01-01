# https://leetcode.com/problems/largest-rectangle-in-histogram/
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
"""


# Brute Force
# Time : O(n^2)
# Space : O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for start in range(0, len(heights)):
            min_height = heights[start]
            for end in range(start, len(heights)):
                min_height = min(min_height, heights[end])
                curr_area = min_height * (end - start + 1)
                max_area = max(max_area, curr_area)

        return max_area


# Divide and Conquer
# Time complexity :
# Average Case: O(nlogn).
# Worst Case: O(n^2) If the numbers in the array are sorted, we don't gain the advantage of divide and conquer.

# Space complexity : O(n). Recursion with worst case depth nn.
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def calculateArea(start, end):
            if start > end:
                return 0
            min_index = start
            for i in range(start, end + 1):
                if heights[min_index] > heights[i]:
                    min_index = i
            return max(heights[min_index] * (end - start + 1), calculateArea(start, min_index - 1), calculateArea(min_index + 1, end))

        return calculateArea(0, len(heights) - 1)


# Using Stack
# Time : O(n)
# Space : O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, ans = [], 0
        for i, h in enumerate(heights + [0]):
            while stack and h <= heights[stack[-1]]:
                H = heights[stack.pop()]
                W = i if not stack else i - stack[-1] - 1
                ans = max(ans, H * W)
            stack.append(i)
        return ans