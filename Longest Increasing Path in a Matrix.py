# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
"""


class Solution:

    rows = 0
    cols = 0
    cache = []

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.rows = len(matrix)
        if self.rows == 0:
            return 0
        self.cols = len(matrix[0])
        self.cache = [[0] * self.cols for i in range(self.rows)]
        ans = 0
        for i in range(self.rows):
            for j in range(self.cols):
                ans = max(ans, self.dfs(matrix, i, j))

        return ans

    def dfs(self, matrix, i, j):
        if self.cache[i][j] != 0:
            return self.cache[i][j]
        val = matrix[i][j]
        self.cache[i][j] = 1 + max(
            self.dfs(matrix, i - 1, j) if i and val > matrix[i - 1][j] else 0,
            self.dfs(matrix, i + 1, j) if i + 1 < self.rows and val > matrix[i + 1][j] else 0,
            self.dfs(matrix, i, j - 1) if j and val > matrix[i][j - 1] else 0,
            self.dfs(matrix, i, j + 1) if j + 1 < self.cols and val > matrix[i][j + 1] else 0,
        )

        return self.cache[i][j]