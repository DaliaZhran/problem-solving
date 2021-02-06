# https://leetcode.com/problems/word-search-ii/

"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
"""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
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

        rows = len(board)
        cols = len(board[0])
        res = []
        for word in words:
            N = len(word)
            out = False
            for i in range(rows):
                for j in range(cols):
                    if search(0, i, j):
                        res.append(word)
                        out = True
                        break
                if out:
                    break
        return res


# Check trie solution -> better in time complexity
# https://leetcode.com/problems/word-search-ii/solution/