# https://leetcode.com/problems/greatest-sum-divisible-by-three/

"""
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
"""


# One Pass
# Time : O(1)
# Space : O(1)
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]  # [sum with remainder of 0, sum with remainder of 1, sum with remainder of 2]
        for num in nums:
            for i in dp[:]:
                dp[(i + num) % 3] = max(dp[(i + num) % 3], i + num)
        return dp[0]