# https://leetcode.com/problems/distinct-subsequences/

"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
"""

# Approach 1: Recursion + Memoization
# Time: O(mn)
# Space: O(mn)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def longestCommonSubsequence(i1, i2):
            if i2 == m:
                return 1

            if i1 == n:
                return 0

            if dp[i1][i2] != -1:
                return dp[i1][i2]

            op1 = 0
            if s[i1] == t[i2]:
                op1 = longestCommonSubsequence(i1 + 1, i2 + 1)

            op2 = longestCommonSubsequence(i1 + 1, i2)

            dp[i1][i2] = op1 + op2
            return dp[i1][i2]

        n = len(s)
        m = len(t)
        dp = [[-1] * m for _ in range(n)]
        return longestCommonSubsequence(0, 0)


# Approach 2: Iterative Dynamic Programming
# Time: O(mn)
# Space: O(mn)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[1] + [0] * m for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]


# Approach 3: Space optimized Dynamic Programming
# Time: O(mn)
# Space: O(m)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [1] + [0] * m

        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[-1]
