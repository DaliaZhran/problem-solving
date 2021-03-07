# https://leetcode.com/problems/longest-palindromic-substring/

"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""


# Approach 1: Produce all substrings and check if each one is a palindrome
# Time: O(n^3) -> O(n^2) for producing all subtrings and O(n) for checking if substring is a palindrome


# Approach : Expand around center -> best sol
# Time: O(n^2)
# space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0

        for i in range(len(s)):
            len1 = self.expand(s, i, i)  # assume odd length, try to extend Palindrome as possible
            len2 = self.expand(s, i, i + 1)  # assume even length
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start : end + 1]

    def expand(self, s, left, right):
        if left > right or s == "":
            return 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1


# Bottom Up DP
# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_palindrome_length = 1
        start_palindrome_index = 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if longest_palindrome_length < end - start + 1:
                            start_palindrome_index = start
                            longest_palindrome_length = end - start + 1

        return s[start_palindrome_index : start_palindrome_index + longest_palindrome_length]


# Approach : Recursive -> not correct -> revisit
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_palindrome_length = 1
        start_palindrome_index = 0
        dp = [[(i, 0)] * n for i in range(n)]

        start_palindrome_index, longest_palindrome_length = self.palindromeLength(s, dp, 0, n - 1)
        return s[start_palindrome_index : start_palindrome_index + longest_palindrome_length]

    def palindromeLength(self, s, dp, start_idx, end_idx):
        if start_idx > end_idx:
            return (start_idx, 0)

        if dp[start_idx][end_idx] != (start_idx, 0):
            return dp[start_idx][end_idx]

        if start_idx == end_idx:
            return (start_idx, 1)

        if s[start_idx] == s[end_idx]:
            remaining = end_idx - start_idx + 1
            if remaining == self.palindromeLength(s, dp, start_idx + 1, end_idx - 1)[1]:
                dp[start_idx][end_idx] = (start_idx, 2 + remaining)
        else:
            op2 = self.palindromeLength(s, dp, start_idx + 1, end_idx)[1]
            op3 = self.palindromeLength(s, dp, start_idx, end_idx - 1)[1]
            dp[start_idx][end_idx] = (start_idx, max(op2, op3))

        return dp[start_idx][end_idx]


# https://leetcode.com/problems/longest-palindromic-substring/discuss/578435/Evolution-from-Recursion-to-Top-Down-DP-to-Bottoms-Up-DP.-Easy-understanding-code
