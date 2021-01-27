# https://leetcode.com/problems/sort-the-matrix-diagonally/

"""
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.
"""

# Heap
# Time: O(m * n * log(min(m,n)))
# Space: O(m * n)
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        diagonals = defaultdict(list)
        for i in range(m):
            for j in range(n):
                heappush(diagonals[i - j], mat[i][j])

        for i in range(m):
            for j in range(n):
                mat[i][j] = heappop(diagonals[i - j])

        return mat


# Sort diagonals one by one
# Time: O(m * n * log(min(m,n)))
# Space: O(min(m,n))
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        def sortDiagonal(i, j):
            diagonal = []
            while i < rows and j < cols:
                heappush(diagonal, -mat[i][j])
                i += 1
                j += 1

            while i > 0 and j > 0:
                i -= 1
                j -= 1
                mat[i][j] = -heappop(diagonal)

        for i in range(rows):
            sortDiagonal(i, 0)

        for j in range(1, cols):
            sortDiagonal(0, j)

        return mat


# Sort diagonals one by one
# Time: O(m * n)
# Space: O(1)
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        # counting sort for each diagonal
        def sortDiagonal(row_index, col_index):
            i, j = row_index, col_index
            diagonal = [0] * 101
            while i < rows and j < cols:
                diagonal[mat[i][j]] += 1
                i += 1
                j += 1

            i, j = row_index, col_index
            for num in range(101):
                while diagonal[num]:
                    mat[i][j] = num
                    i += 1
                    j += 1
                    diagonal[num] -= 1

        # sort diagonals who start in the first col
        for i in range(rows):
            sortDiagonal(i, 0)

        # sort diagonals who start in the first row
        for j in range(1, cols):
            sortDiagonal(0, j)

        return mat