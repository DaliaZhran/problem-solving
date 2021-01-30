# https://leetcode.com/problems/n-queens-ii/

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""


class Solution:
    cnt = 0

    def totalNQueens(self, n: int) -> int:
        col_ids = [-1] * n
        path = [["."] * n for _ in range(n)]
        self.explore(0, col_ids, path, n)
        return self.cnt

    def explore(self, row, col_ids, path, n):
        if row == n:
            self.cnt += 1

        for col in range(n):
            if self.isValid(col_ids, row, col):
                col_ids[row] = col
                path[row][col] = "Q"
                self.explore(row + 1, col_ids, path, n)
                path[row][col] = "."

    def isValid(self, col_ids, row, col):
        for i in range(row):
            if col_ids[i] == col or abs(col_ids[i] - col) == abs(row - i):
                return False
        return True
