# https://leetcode.com/problems/palindromic-substrings/


"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
"""


# Approach 1: Produce all substrings and check if each one is a palindrome
# Time: O(n^3) -> O(n^2) for producing all subtrings and O(n) for checking if substring is a palindrome


# Bottom Up DP
# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            count += 1

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        count += 1

        return count


# Approach : Expand around center -> best sol
# Time: O(n^2)
# space: O(1)
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return ""

        start, end = 0, 0
        count = 0

        for i in range(len(s)):
            count += self.expand(s, i, i)  # assume odd length, try to extend Palindrome as possible
            count += self.expand(s, i, i + 1)  # assume even length

        return count

    def expand(self, s, left, right):
        if left > right or s == "":
            return 0

        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            count += 1

        return count
