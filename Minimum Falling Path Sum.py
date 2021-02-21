# https://leetcode.com/problems/minimum-falling-path-sum/

"""
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
"""


# Brute Force - Recursive
# Time: O(3^rows)
# Space: O(rows)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def min_path(r, c, curr):
            nonlocal min_sum
            if c < 0 or c >= cols:
                return 0
            if r == rows - 1:
                min_sum = min(curr + matrix[r][c], min_sum)
            else:
                min_path(r + 1, c - 1, curr + matrix[r][c])
                min_path(r + 1, c, curr + matrix[r][c])
                min_path(r + 1, c + 1, curr + matrix[r][c])

        rows = len(matrix)
        cols = len(matrix[0])

        min_sum = float("inf")
        for i in range(cols):
            min_path(0, i, 0)
        return min_sum


# Direct Recursion
# Time: O(3^rows)
# Space: O(rows)
# Idea is same as postorder traversal
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def min_path(r, c):
            if c < 0 or c >= cols:
                return float("inf")
            if r == rows - 1:
                return matrix[r][c]

            value = matrix[r][c]
            min_sum = min(min_path(r + 1, c - 1) + value, min_path(r + 1, c) + value, min_path(r + 1, c + 1) + value)

            return min_sum

        rows = len(matrix)
        cols = len(matrix[0])
        min_sum = float("inf")
        for i in range(cols):
            min_sum = min(min_sum, min_path(0, i, 0))
        return min_sum


# Same as before  but with passing curr sum
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def min_path(r, c, curr):
            if c < 0 or c >= cols:
                return float("inf")
            if r == rows - 1:
                return curr + matrix[r][c]

            value = matrix[r][c]
            min_sum = min(min_path(r + 1, c - 1, curr + value), min_path(r + 1, c, curr + value), min_path(r + 1, c + 1, curr + value))

            return min_sum

        rows = len(matrix)
        cols = len(matrix[0])
        min_sum = float("inf")
        for i in range(cols):
            min_sum = min(min_sum, min_path(0, i, 0))
        return min_sum


# DP (Memoization)
# Time: O(rows * cols)
# Space: O(rows)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def min_path(r, c):
            if c < 0 or c >= cols:
                return float("inf")
            if r == rows - 1:
                return matrix[r][c]

            if dp[r][c] != None:
                return dp[r][c]

            value = matrix[r][c]
            min_sum = min(min_path(r + 1, c - 1) + value, min_path(r + 1, c) + value, min_path(r + 1, c + 1) + value)

            dp[r][c] = min_sum
            return min_sum

        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[None] * cols for _ in range(rows)]
        min_sum = float("inf")
        for i in range(cols):
            min_sum = min(min_sum, min_path(0, i, 0))
        return min_sum


# Iterative
# Time: O(rows * cols)
# Space: O(1)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(1, rows):
            for j in range(cols):
                prev_col = max(j - 1, 0)
                next_col = min(j + 1, cols - 1)
                matrix[i][j] += min(matrix[i - 1][prev_col], matrix[i - 1][j], matrix[i - 1][next_col])

        return min(matrix[-1])


# https://leetcode.com/problems/minimum-falling-path-sum/discuss/381898/Python-Not-shortest-but-easiest-to-understand-with-explanation