# https://leetcode.com/problems/edit-distance/


"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
"""


# we can remove memoization to get a normal recursive solution
# Time: O(M*N) -> m = len(word1) and n = len(word2)
# Space: O(M*N)
class Solution:
    dp = {}

    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) or len(word2)

        if self.dp.get((word1, word2), 0):
            return self.dp[(word1, word2)]

        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        insert = 1 + self.minDistance(word1, word2[1:])
        delete = 1 + self.minDistance(word1[1:], word2)
        replace = 1 + self.minDistance(word1[1:], word2[1:])

        self.dp[(word1, word2)] = min(insert, delete, replace)
        return self.dp[(word1, word2)]


# Same solution but using iterators instead of string slicing
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(i, j):
            if i == m or j == n:
                return m - i or n - j

            if dp.get((i, j), 0):
                return dp[(i, j)]

            if word1[i] == word2[j]:
                return solve(i + 1, j + 1)
            insert = 1 + solve(i, j + 1)
            delete = 1 + solve(i + 1, j)
            replace = 1 + solve(i + 1, j + 1)

            dp[(i, j)] = min(insert, delete, replace)
            return dp[(i, j)]

        dp = {}
        m = len(word1)
        n = len(word2)
        return solve(0, 0)


# Iterative DP
# Time: O(m*n) -> m = len(word1) and n = len(word2)
# Space: O(m*n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m * n == 0:
            return m or n
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

        return dp[m][n]


# https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition

# Fine Tuning of space complexity
# https://leetcode.com/problems/edit-distance/discuss/25846/C%2B%2B-O(n)-space-DP