# https://leetcode.com/problems/partition-equal-subset-sum/

"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""

from functools import lru_cache

# Recursive Brute Force -> try all possible subsets [TLE]
# Time: (2^n)
# Space: (n)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # @lru_cache(maxsize=None) -> decorator to use memoization
        def solve(index, sum):
            if sum == 0:
                return True
            if sum < 0 or index == n:
                return False
            return solve(index + 1, sum) or solve(index + 1, sum - nums[index])

        n = len(nums)
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        return solve(0, total_sum // 2)


# Using DP
# Time: O(N * S/2) -> N is len(nums), S is sum(nums)
# Space: O(N * S/2)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        dp = [[True] + [False] * (total_sum // 2) for _ in range(n)]

        for i in range(n):
            for s in range(total_sum // 2 + 1):
                if s - nums[i] < 0:
                    dp[i][s] = dp[i - 1][s]
                else:
                    dp[i][s] = dp[i - 1][s] or dp[i - 1][s - nums[i]]

        return dp[-1][-1]


# Using DP -> Fine Tuning for space
# Time: O(N * S/2) -> N is len(nums), S is sum(nums)
# Space: O(S/2)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False

        total_sum = sum(nums)
        if total_sum % 2:
            return False
        subset_sum = total_sum // 2

        dp = [False] * (subset_sum + 1)
        dp[0] = True

        for curr in nums:
            for s in range(subset_sum, curr - 1, -1):
                dp[s] = dp[s] or dp[s - curr]

        return dp[-1]


"""
The essence of using 1D dp is the we must start backward. In Approach 3, we are using the result of previous row. IIn Approach 4, since we are using single row, if you start from front, you are changing the previous values without calculating the current values.
We are using dp[j - curr] value to calculate value of current j. Eg, if j = 4, curr = 2.
You are using value of dp[2] {j-curr} to calculate value of dp[4] (j). So if you change value of dp[2] before calculating value of dp[4], it would be wrong.
Hence, you have to start from back in 1D dp solution.
"""


# TO DO: check the same ideas but starting from the last element