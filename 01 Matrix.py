# https://leetcode.com/problems/01-matrix/


# Brute Force Solution [Time Limit Exceeded]
# Time : O(rows * cols)^2
# Space : O(rows * cols)
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        if rows == 0:
            return matrix
        cols = len(matrix[0])

        dist = [[float("inf") for _ in range(cols)] for __ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    for k in range(rows - 1, -1, -1):
                        for l in range(cols - 1, -1, -1):
                            if matrix[k][l] == 0:
                                curr_dist = abs(k - i) + abs(l - j)
                                dist[i][j] = min(dist[i][j], curr_dist)

        return dist


# BFS Solution
# Time : O(rows * cols)
# Space : O(rows * cols)
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        if rows == 0:
            return matrix
        cols = len(matrix[0])

        dist = [[float("inf") for _ in range(cols)] for __ in range(rows)]
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))  # Put all 0s in the queue.

        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # up, right, down, left
        while queue:
            curr_row, curr_col = queue.popleft()
            for i in range(4):
                new_row = curr_row + directions[i][0]
                new_col = curr_col + directions[i][1]
                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                    temp = dist[curr_row][curr_col] + 1
                    if dist[new_row][new_col] > temp:
                        dist[new_row][new_col] = temp
                        queue.append((new_row, new_col))

        return dist


# DP Solution
# Time : O(rows * cols)
# Space : O(rows * cols)
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        if rows == 0:
            return matrix
        cols = len(matrix[0])

        dist = [[float("inf") for _ in range(cols)] for __ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                else:
                    # neighbor above
                    if i > 0:
                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                    # neighbor on left
                    if j > 0:
                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                # neighbor below
                if i < rows - 1:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                # neighbor on right
                if j < cols - 1:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)

        return dist