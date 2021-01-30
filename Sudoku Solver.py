# https://leetcode.com/problems/sudoku-solver/
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
"""

# Brute Force
# With no constraints, given a 9x9 board we have at max 81 spaces where in each space we can place the number 1-9 (but on a normal board many spaces will already have a number before we even start solving)

# This means that there are 9^81 total arrangements of the board (as a loose upper bound). This is 1.9662705 * 10 ^ 77 boards just for a 9 x 9 board.


# Approach 2: Backtracking
# with 9 * 9 board, nothing can scale but if for n * n board, it would be a NP-Complete problem
# Time: O(9^m) where m is the number of cells to be filled since each one has 9 possible solution at most
# OR O(9!^9) since for each row we have 9! permutations and we do this for the 9 rows
# Space: O(1)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0, 0)

    def solve(self, board, row, col):
        # solve for each row
        for i in range(row, 9):
            # solve for each col
            for j in range(col, 9):
                # if cell not empty, then continue
                if board[i][j] != ".":
                    continue
                # check all possible numbers we can fill the cell with
                for num in range(1, 10):
                    num = str(num)
                    # if a num is valid, we go continue to solve for the rest
                    if self.isValid(board, num, i, j):
                        board[i][j] = num
                        if self.solve(board, i, j + 1):
                            return True
                        # if we could not find a solution with the number we chose before, we backtrack and check another num
                        board[i][j] = "."
                # if all numbers failed to find a solution, then we cannot find a solution for the current state and we should backtrack
                return False
            col = 0
        return True

    def isValid(self, board, num, row, col):
        blkrow = row - row % 3
        blkcol = col - col % 3
        for i in range(9):
            if board[i][col] == num or board[row][i] == num or board[blkrow + i // 3][blkcol + i % 3] == num:
                return False
        return True

    # another implementation
    # def isValid(self, board, num, row, col):
    #     blkrow = (row // 3) * 3
    #     blkcol = (col // 3) * 3
    #     for i in range(9):
    #         if board[i][col] == num or board[row][i] == num or board[blkrow + i // 3][blkcol + i % 3] == num:
    #             return False
    #     return True;


# Just a small improvement of time for knoweldge
class Solution:
    def box_index(self, row: int, col: int) -> int:
        return (row // 3) * 3 + col // 3

    def solve(self, empty_cells) -> bool:
        if not empty_cells:
            return True

        row, col = empty_cells.pop()
        for num in range(1, 10):
            box_index = self.box_index(row, col)
            if num not in self.rows[row] and num not in self.cols[col] and num not in self.boxes[box_index]:
                self.rows[row].add(num)
                self.cols[col].add(num)
                self.boxes[box_index].add(num)
                self.board[row][col] = str(num)

                solved = self.solve(empty_cells)
                if solved:
                    return solved

                # Back track
                self.board[row][col] = "."
                self.rows[row].remove(num)
                self.cols[col].remove(num)
                self.boxes[box_index].remove(num)

        empty_cells.append((row, col))

        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for row in range(9)]
        cols = [set() for col in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num = int(board[row][col])
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[self.box_index(row, col)].add(num)
                else:
                    empty_cells.append((row, col))

        self.rows = rows
        self.cols = cols
        self.boxes = boxes
        self.board = board
        return self.solve(empty_cells)


# https://leetcode.com/problems/sudoku-solver/discuss/15853/Simple-and-Clean-Solution-C%2B%2B

"""
The 3 Keys To Backtracking:

Our Choice

What we place in an empty cell that we see.

Our Constraints

Standard Sudoku constraints. We cannot make a placement that will break the board.

Our Goal

Place all empty spaces on the board. We will know we have done this when we have placed a valid value in the last cell in our search which programmatically will be the bottom right cell in the 2D matrix.
"""
