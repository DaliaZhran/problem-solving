# https://leetcode.com/problems/spiral-matrix/


# Approach 1: Simulation
# Time : O(rows*cols)
# Space : O(rows*cols)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        if rows == 0:
            return matrix
        cols = len(matrix[0])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # right, down, left, up
        result = []
        visited = set()
        x, y, curr_dir = 0, 0, 0
        for _ in range(rows * cols):
            result.append(matrix[x][y])
            visited.add((x, y))
            new_x = x + directions[curr_dir][0]
            new_y = y + directions[curr_dir][1]
            if new_x >= 0 and new_x < rows and new_y >= 0 and new_y < cols and (new_x, new_y) not in visited:
                x = new_x
                y = new_y
            else:
                curr_dir = (curr_dir + 1) % 4
                x = x + directions[curr_dir][0]
                y = y + directions[curr_dir][1]

        return result


# Approach 2: Layer-by-Layer
# Time : O(rows*cols)
# Space : O(1) without the output and O(rows*cols) if we consider output
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        row1 = 0
        col1 = 0
        row2 = len(matrix) - 1
        col2 = len(matrix[0]) - 1
        result = []

        while row1 <= row2 and col1 <= col2:
            # up
            for c in range(col1, col2 + 1):
                result.append(matrix[row1][c])
            # right
            for r in range(row1 + 1, row2 + 1):
                result.append(matrix[r][col2])

            if row1 < row2 and col1 < col2:
                # down
                for c in range(col2 - 1, col1, -1):
                    result.append(matrix[row2][c])
                # left
                for r in range(row2, row1, -1):
                    result.append(matrix[r][col1])

            row1 += 1
            row2 -= 1
            col1 += 1
            col2 -= 1

        return result