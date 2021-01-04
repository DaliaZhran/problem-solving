# https://leetcode.com/problems/number-of-islands/
"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""

# DFS
# Time : O(M x N)
# Space : O(M x N)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            grid[row][col] = 0

            if row - 1 >= 0 and grid[row - 1][col] == "1":  # up
                dfs(row - 1, col)
            if row + 1 < rows and grid[row + 1][col] == "1":  # down
                dfs(row + 1, col)
            if col - 1 >= 0 and grid[row][col - 1] == "1":  # left
                dfs(row, col - 1)
            if col + 1 < cols and grid[row][col + 1] == "1":  # right
                dfs(row, col + 1)

        if rows == 0:
            return 0

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count


# BFS
# Time : O(M x N)
# Space : O(min(M, N)) -> https://imgur.com/gallery/M58OKvB
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        if rows == 0:
            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    neighbors = deque([(i, j)])
                    grid[i][j] = 0
                    while neighbors:
                        row, col = neighbors.popleft()
                        if row - 1 >= 0 and grid[row - 1][col] == "1":  # up
                            neighbors.append((row - 1, col))
                            grid[row - 1][col] = 0
                        if row + 1 < rows and grid[row + 1][col] == "1":  # down
                            neighbors.append((row + 1, col))
                            grid[row + 1][col] = 0
                        if col - 1 >= 0 and grid[row][col - 1] == "1":  # left
                            neighbors.append((row, col - 1))
                            grid[row][col - 1] = 0
                        if col + 1 < cols and grid[row][col + 1] == "1":  # right
                            neighbors.append((row, col + 1))
                            grid[row][col + 1] = 0

        return count
