# https://leetcode.com/problems/target-sum/

"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
"""

# Can be solved first with recursion and memoization

# 2D DP -> knapsack
# Time: O(N * C) where C is (S + total_sum) // 2
# Space: O(N * C)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        def subsetSum(target_sum):
            dp = [[1] + [0] * (target_sum) for _ in range(n)]

            for i in range(n):
                for s in range(target_sum + 1):
                    if s - nums[i] < 0:
                        dp[i][s] = dp[i - 1][s]
                    else:
                        dp[i][s] = dp[i - 1][s] + dp[i - 1][s - nums[i]]

            return dp[-1][-1]

        n = len(nums)
        total_sum = sum(nums)
        if total_sum < S or (S + total_sum) % 2 == 1:
            return 0

        target_sum = (S + total_sum) // 2
        return subsetSum(target_sum)


# 1D DP
# Time: O(N * C) where C is (S + total_sum) // 2
# Space: O(C)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        total_sum = sum(nums)
        if total_sum < S or (S + total_sum) % 2 == 1:
            return 0

        target_sum = (S + total_sum) // 2
        dp = [1] + [0] * target_sum

        for n in nums:
            for s in range(target_sum, n - 1, -1):
                dp[s] += dp[s - n]

        return dp[-1]


# https://leetcode.com/problems/target-sum/discuss/455024/DP-IS-EASY!-5-Steps-to-Think-Through-DP-Questions.