# https://leetcode.com/problems/minimum-path-sum/

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


# Recursive (Brute Force), then DP -> https://leetcode.com/problems/minimum-path-sum/discuss/344980/Java.-Details-from-Recursion-to-DP.
# Basic Sol with tuning -> https://leetcode.com/problems/minimum-path-sum/discuss/23457/C%2B%2B-DP


# Recursive (Brute Force)
# Time: O(2^max(m,n))
# Space: O(max(m,n))
# Implementation can be more clear if we started from the end to (0,0) instead and use direct recursion instead of side effect
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def helper(i, j):
            if i == m or j == n:
                return float("inf")
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            return grid[i][j] + min(helper(i + 1, j), helper(i, j + 1))

        m = len(grid)
        n = len(grid[0])
        return helper(0, 0)


# DP (2D) -> Bottom Up
# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def helper(i, j):
            if i == m or j == n:
                return float("inf")
            if dp[i][j] != -1:
                return dp[i][j]
            if i == m - 1 and j == n - 1:
                return grid[i][j]

            dp[i][j] = grid[i][j] + min(helper(i + 1, j), helper(i, j + 1))
            return dp[i][j]

        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        return helper(0, 0)


# DP (2D) -> Bottom Up
# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i > 0 and j > 0:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
                elif i > 0 and j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                elif i == 0 and j > 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                else:
                    dp[i][j] = grid[i][j]

        return dp[-1][-1]


# Optimization -> DP 1D -> use 2 cols for holding the needed cols only
# Time: O(mn)
# Space: O(m)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        cur = [0] * rows  # Vector for current column sums
        pre = [0] * rows  # Vector for previous column sums
        pre[0] = grid[0][0]

        for i in range(1, rows):
            pre[i] = pre[i - 1] + grid[i][0]

        for j in range(1, cols):
            cur[0] = pre[0] + grid[0][j]
            for i in range(1, rows):
                cur[i] = min(cur[i - 1], pre[i]) + grid[i][j]

            pre = cur

        return pre[rows - 1]


# Optimization -> DP 1D -> use 1 col for holding the needed sum, sone value before update and one after update
# Time: O(mn)
# Space: O(m)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        cur = [0] * rows  # Vector for current column sums
        cur[0] = grid[0][0]

        for i in range(1, rows):
            cur[i] = cur[i - 1] + grid[i][0]

        for j in range(1, cols):
            cur[0] = cur[0] + grid[0][j]
            for i in range(1, rows):
                cur[i] = min(cur[i - 1], cur[i]) + grid[i][j]

        return cur[rows - 1]
