# https://leetcode.com/problems/longest-increasing-subsequence/

"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""


# Brute Force
# Time: O(2 ^ n), where n is length of nums
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def helper(last_pos, start):
            if start >= n:
                return 0

            count1 = 0
            if last_pos == -1 or nums[start] > nums[last_pos]:
                count1 = 1 + helper(start, start + 1)

            count2 = helper(last_pos, start + 1)
            return max(count1, count2)

        n = len(nums)
        if n < 2:
            return n
        return helper(-1, 0)


# Top-down Dynamic Programming with Memoization
# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def helper(last_pos, curr):
            if curr >= n:
                return 0

            if dp[curr][last_pos] == -1:
                count1 = 0
                if last_pos == -1 or nums[curr] > nums[last_pos]:
                    count1 = 1 + helper(curr, curr + 1)

                count2 = helper(last_pos, curr + 1)
                dp[curr][last_pos] = max(count1, count2)

            return dp[curr][last_pos]

        n = len(nums)
        if n < 2:
            return n
        dp = [[-1] * (n + 1) for _ in range(n)]
        return helper(-1, 0)


# Bottom-up Dynamic Programming
# Time: O(n^2)
# Space: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        dp = [0] * n
        dp[0] = 1

        max_length = 1
        for i in range(1, n):
            dp[i] = 1
            for j in range(i):
                if nums[i] > nums[j] and dp[i] <= dp[j]:
                    dp[i] = 1 + dp[j]
                    max_length = max(max_length, dp[i])

        return max_length
