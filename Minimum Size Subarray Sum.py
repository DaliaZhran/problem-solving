# https://leetcode.com/problems/minimum-size-subarray-sum/
"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""


# Sliding Window
# Time: O(N)
# Space: O(1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_len = n + 1
        start = 0

        for end, end_val in enumerate(nums):
            target -= end_val
            while start <= end and target <= 0:
                min_len = min(min_len, end - start + 1)
                target += nums[start]
                start += 1

        return 0 if min_len == n + 1 else min_len


# Check other solutions
