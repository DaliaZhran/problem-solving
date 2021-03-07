# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

"""
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.
"""

# Top Down Memoization
# Time: O(n^2) where n is length of s
# Space: O(n^2)
class Solution:
    def minInsertions(self, s: str) -> int:
        def palindromeLength(start_idx, end_idx):
            if start_idx > end_idx:
                return 0

            if dp[start_idx][end_idx] != 0:
                return dp[start_idx][end_idx]

            if start_idx == end_idx:
                return 1

            if s[start_idx] == s[end_idx]:
                dp[start_idx][end_idx] = 2 + palindromeLength(start_idx + 1, end_idx - 1)
            else:
                op2 = palindromeLength(start_idx + 1, end_idx)
                op3 = palindromeLength(start_idx, end_idx - 1)
                dp[start_idx][end_idx] = max(op2, op3)

            return dp[start_idx][end_idx]

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        return n - palindromeLength(0, n - 1)


# Bottom Up DP
# Time: O(n^2) where n is length of s
# Space: O(n^2)
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for start_idx in range(n - 1, -1, -1):
            for end_idx in range(start_idx + 1, n):
                if s[start_idx] == s[end_idx]:
                    dp[start_idx][end_idx] = 2 + dp[start_idx + 1][end_idx - 1]
                else:
                    dp[start_idx][end_idx] = max(dp[start_idx + 1][end_idx], dp[start_idx][end_idx - 1])

        return n - dp[0][-1]


# Reducing Space
# Time: O(n^2) where n is length of s
# Space: O(n)
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)

        prev_row = [0] * n
        prev_row[-1] = 1
        for start_idx in range(n - 1, -1, -1):
            curr_row = [0] * n
            curr_row[start_idx] = 1
            for end_idx in range(start_idx + 1, n):
                if s[start_idx] == s[end_idx]:
                    curr_row[end_idx] = 2 + prev_row[end_idx - 1]
                else:
                    curr_row[end_idx] = max(prev_row[end_idx], curr_row[end_idx - 1])

            prev_row = curr_row

        return n - curr_row[-1]
