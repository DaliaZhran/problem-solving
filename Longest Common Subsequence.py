# https://leetcode.com/problems/longest-common-subsequence/

"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
"""

# Brute Force
# Time: O(3 ^ (n + m)), where n is length of text1 and m is length of text2
# Space: O(n + m) for stack
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def longestCommonSubsequenceRecursive(i1, i2):
            if i1 == n or i2 == m:
                return 0

            if text1[i1] == text2[i2]:
                return 1 + longestCommonSubsequenceRecursive(i1 + 1, i2 + 1)

            op1 = longestCommonSubsequenceRecursive(i1 + 1, i2)
            op2 = longestCommonSubsequenceRecursive(i1, i2 + 1)
            return max(op1, op2)

        n = len(text1)
        m = len(text2)
        return longestCommonSubsequenceRecursive(0, 0)


# Top-down Dynamic Programming with Memoization
# Time: O(n * m)
# Space: O(n * m)
class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def longestCommonSubsequenceRecursive(i1, i2):
            if i1 == n or i2 == m:
                return 0

            if dp[i1][i2] != -1:
                return dp[i1][i2]

            if text1[i1] == text2[i2]:
                dp[i1][i2] = 1 + longestCommonSubsequenceRecursive(i1 + 1, i2 + 1)
            else:
                op1 = longestCommonSubsequenceRecursive(i1 + 1, i2)
                op2 = longestCommonSubsequenceRecursive(i1, i2 + 1)
                dp[i1][i2] = max(op1, op2)

            return dp[i1][i2]

        n = len(text1)
        m = len(text2)
        dp = [[-1] * m for _ in range(n)]
        return longestCommonSubsequenceRecursive(0, 0)


# Bottom-up Dynamic Programming
# Time: O(n * m)
# Space: O(n * m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]  # the +1 col and row to avoid checking for i - 1 and j - 1

        max_length = -1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                max_length = max(max_length, dp[i][j])
        return max_length


# we can further optimize the space by keeping only the prev row
