# https://leetcode.com/problems/number-of-matching-subsequences/

"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
"""


# check word by word -> TLE
# Time: O(k * n * c), where k is len(words)
# Space: O(n * c), where c is the max length of strings in list words
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def lcs(s1, s2):
            dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            return dp[-1][-1]

        count = 0
        n = len(s)
        for w in words:
            m = len(w)
            lcs_len = lcs(s, w)
            if lcs_len == m:
                count += 1
        return count
