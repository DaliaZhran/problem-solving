# https://leetcode.com/problems/perfect-squares/

"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 
Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
"""

from math import sqrt, floor


# Recursive - TLE
# Time: O(sqrt(n)^n)
# Space: O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        if n < 0:
            return -1

        if n == 0:
            return 0

        min_count = float("inf")
        end_range = floor(sqrt(n)) + 1
        for i in range(1, end_range):
            count = 1 + self.numSquares(n - i * i)
            if count != -1:
                min_count = min(min_count, count)

        return min_count


# Recursive & Memoization
# Time: O(n * sqrt(n))
# Space: O(n)
class Solution:
    dp = {}

    def numSquares(self, n: int) -> int:
        if n < 0:
            return -1

        if n == 0:
            return 0

        if self.dp.get(n, 0):
            return self.dp[n]

        min_count = float("inf")
        end_range = floor(sqrt(n)) + 1
        for i in range(1, end_range):
            count = 1 + self.numSquares(n - i * i)
            if count != -1:
                min_count = min(min_count, count)

        self.dp[n] = min_count

        return min_count


# Recursive & Memoization
# Time: O(n * sqrt(n))
# Space: O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, floor(sqrt(n)) + 1):
                square = j * j
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]
