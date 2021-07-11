# https://leetcode.com/problems/climbing-stairs/
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""

# Brute Force - Bottom Up Recursive
# Time : O(2^n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# Recursive with Memoization
# Time : O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        def climbStairsRecursive(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]

            memo[i] = climbStairsRecursive(i + 1) + climbStairsRecursive(i + 2)
            return memo[i]

        memo = {}
        return climbStairsRecursive(0)


# Approach 4: DP
# Time : O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# Approach 4: Fibonacci Number
# Time : O(n)
# Space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        prev1 = prev2 = 1
        for i in range(2, n + 1):
            prev1, prev2 = prev2, prev1 + prev2
        return prev2
