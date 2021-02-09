# https://leetcode.com/problems/minimum-path-sum/

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""


# Recursive (Brute Force), then DP -> https://leetcode.com/problems/minimum-path-sum/discuss/344980/Java.-Details-from-Recursion-to-DP.
# Basic Sol with tuning -> https://leetcode.com/problems/minimum-path-sum/discuss/23457/C%2B%2B-DP


# DP (2D)
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


# Optimization -> DP 1D