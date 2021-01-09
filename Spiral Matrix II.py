# https://leetcode.com/problems/spiral-matrix-ii/


# Approach 1: Layer-by-Layer
# Time : O(rows*cols)
# Space : O(1) without the output and O(rows*cols) if we consider output
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        row1 = 0
        col1 = 0
        row2 = n - 1
        col2 = n - 1
        result = [[0] * n for _ in range(n)]
        counter = 1
        while row1 <= row2 and col1 <= col2:
            # up
            for c in range(col1, col2 + 1):
                result[row1][c] = counter
                counter += 1
            # right
            for r in range(row1 + 1, row2 + 1):
                result[r][col2] = counter
                counter += 1

            if row1 < row2 and col1 < col2:
                # down
                for c in range(col2 - 1, col1, -1):
                    result[row2][c] = counter
                    counter += 1
                # left
                for r in range(row2, row1, -1):
                    result[r][col1] = counter
                    counter += 1

            row1 += 1
            row2 -= 1
            col1 += 1
            col2 -= 1

        return result