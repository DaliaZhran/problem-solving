# https://leetcode.com/problems/fibonacci-number/
"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).
"""


# Approach 1: Recursion
# Time : O(2^n)
# Space: O(n)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


# Approach 2: Bottom-Up Approach using Memoization
# Time : O(n)
# Space: O(n)
class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        for i in range(2, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]


# Approach 3: Top-Down Approach using Memoization
# Time : O(n)
# Space: O(n)
class Solution:
    dp = defaultdict(int)

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        if self.dp[n] != 0:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


# Approach 4: Iterative Top-Down Approach
# Time : O(n)
# Space: O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        prev1 = 0
        prev2 = 1
        for i in range(2, n + 1):
            prev1, prev2 = prev2, prev1 + prev2
        return prev2
