# https://leetcode.com/problems/word-search/

"""
Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""


# Backtracking
# Time: O(N*4*3^min(L, N)) -> N is number of cells and L is len(word)
# Space: O(L)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(index, row, col):
            if index == N:
                return True

            if row < 0 or row == rows or col < 0 or col == cols or word[index] != board[row][col]:
                return False

            found = False
            board[row][col] = "#"
            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                found = search(index + 1, row + row_offset, col + col_offset)
                if found:
                    break
            board[row][col] = word[index]
            return found

        N = len(word)
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if search(0, i, j):
                    return True
        return False
