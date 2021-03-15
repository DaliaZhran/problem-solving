# https://leetcode.com/problems/unique-paths/


# Brute Force
# Time: O(2^mn)
# Space: O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def uniquePathsRecursive(r, c):
            if r == m - 1 or c == n - 1:
                return 1

            return uniquePathsRecursive(r, c + 1) + uniquePathsRecursive(r + 1, c)

        return uniquePathsRecursive(0, 0)


# Top Down with memoization
# Time: O(mn)
# Space: O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def uniquePathsRecursive(r, c):
            if r == m - 1 or c == n - 1:
                return 1

            if dp[r][c] != -1:
                return dp[r][c]

            dp[r][c] = uniquePathsRecursive(r, c + 1) + uniquePathsRecursive(r + 1, c)
            return dp[r][c]

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return uniquePathsRecursive(0, 0)


# Bottom Up DP
# Time: O(mn)
# Space: O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


# Optimized DP
# Time: O(mn)
# Space: O(n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for _ in range(n)]
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]

        return dp[-1]
