# https://leetcode.com/problems/longest-repeating-substring/

"""
Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

 
Example 2:

Input: S = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
"""

# Brute Force -> TLE
# Time: O(2^n)
# Space: O(n)
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        def longestRepeatingSubstringRecursive(i1: int, i2: int, count: int) -> int:
            if i1 == n or i2 == n:
                return count

            if i1 != i2 and S[i1] == S[i2]:
                count = longestRepeatingSubstringRecursive(i1 + 1, i2 + 1, count + 1)

            c1 = longestRepeatingSubstringRecursive(i1 + 1, i2, 0)
            c2 = longestRepeatingSubstringRecursive(i1, i2 + 1, 0)

            return max(count, c1, c2)

        n = len(S)
        return longestRepeatingSubstringRecursive(0, 0, 0)


# Top-down Dynamic Programming with Memoization -> TLE
# Time: O(n^2)
# Space: O(n^3)
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        def longestRepeatingSubstringRecursive(i1: int, i2: int, count: int) -> int:
            if i1 == n or i2 == n:
                return count

            if dp[i1][i2][count] != -1:
                return dp[i1][i2][count]

            c1 = count
            if i1 != i2 and S[i1] == S[i2]:
                c1 = longestRepeatingSubstringRecursive(i1 + 1, i2 + 1, count + 1)

            c2 = longestRepeatingSubstringRecursive(i1 + 1, i2, 0)
            c3 = longestRepeatingSubstringRecursive(i1, i2 + 1, 0)

            dp[i1][i2][count] = max(c1, c2, c3)
            return dp[i1][i2][count]

        n = len(S)
        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        return longestRepeatingSubstringRecursive(0, 0, 0)


# Bottom-up Dynamic Programming
# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        max_length = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j and S[i - 1] == S[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    max_length = max(max_length, dp[i][j])

        return max_length


# Bottom-up Dynamic Programming - Reducing Space
# Time: O(n^2)
# Space: O(n)
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        prev_row = [0 for _ in range(n + 1)]

        max_length = 0
        for i in range(1, n + 1):
            curr_row = [0 for _ in range(n + 1)]
            for j in range(i + 1, n + 1):
                if S[i - 1] == S[j - 1]:
                    curr_row[j] = 1 + prev_row[j - 1]
                    max_length = max(max_length, curr_row[j])
            prev_row = curr_row

        return max_length


# Check other solutions -> Binary Search, Trie, Suffix Tree
