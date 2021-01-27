# https://leetcode.com/problems/n-queens/

"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col_ids = [-1] * n
        path = [["."] * n for _ in range(n)]
        self.explore(0, col_ids, path, res, n)
        return res

    def explore(self, row, col_ids, path, res, n):
        if row == n:
            res.append(["".join(path[i]) for i in range(n)])

        for col in range(n):
            if self.isValid(col_ids, row, col):
                col_ids[row] = col
                path[row][col] = "Q"
                self.explore(row + 1, col_ids, path, res, n)
                path[row][col] = "."

    def isValid(self, col_ids, row, col):
        for i in range(row):
            if col_ids[i] == col or abs(col_ids[i] - col) == abs(row - i):
                return False
        return True
