# https://leetcode.com/problems/maximum-subarray/

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
from typing import List

# Brute Force -> O(n^2)

# Sliding Window
# Time: O(n) where n is the length of nums
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        curr_sum = 0
        start = 0
        for end in range(len(nums)):
            curr_sum += nums[end]
            max_sum = max(max_sum, curr_sum)  # check the max (if the number is -ve, it will be considered too)
            # we do not need our sum to be -ve because if we kept it -ve, we will make the overall/next sum smaller
            while curr_sum < 0 and start <= end:
                curr_sum -= nums[start]
                start += 1
        return max_sum


# DP
# Time: O(n)
# Space: O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]  # 1 <= len(nums) <= 3 * 10^4
        max_sum = dp[0]
        for i in range(1, n):
            dp[i] = nums[i] if dp[i - 1] < 0 else nums[i] + dp[i - 1]
            max_sum = max(max_sum, dp[i])
        return max_sum


# DP Optimized
# Time: O(n)
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = curr_sum = nums[0]
        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum


# check divide and conquer
