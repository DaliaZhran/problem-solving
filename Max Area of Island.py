# https://leetcode.com/problems/max-area-of-island/

"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
"""

# DFS
# Time: O(rows * cols)
# Space: O(rows * cols)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def solve(r, c):
            nonlocal max_area
            if r < 0 or r == rows or c < 0 or c == cols:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            curr_area = 1 + solve(r + 1, c) + solve(r - 1, c) + solve(r, c + 1) + solve(r, c - 1)
            max_area = max(curr_area, max_area)
            return curr_area

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    solve(i, j)
        return max_area


# Better Imp
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def solve(r, c):
            if r < 0 or r == rows or c < 0 or c == cols:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + solve(r + 1, c) + solve(r - 1, c) + solve(r, c + 1) + solve(r, c - 1)

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, solve(i, j))
        return max_area


# Use set to track visited cells instead of modifying the actuall list
# Time: O(rows * cols)
# Space: O(rows * cols)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()

        def solve(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in seen or grid[r][c] == 0:
                return 0
            seen.add((r, c))
            return 1 + solve(r + 1, c) + solve(r - 1, c) + solve(r, c + 1) + solve(r, c - 1)

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                max_area = max(max_area, solve(i, j))
        return max_area


# Iterative DFS
# Time: O(rows * cols)
# Space: O(rows * cols)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        seen = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and grid[i][j] not in seen:
                    stack = [(i, j)]
                    seen.add((i, j))
                    curr_area = 0
                    while stack:
                        r, c = stack.pop()
                        curr_area += 1
                        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] and (nr, nc) not in seen:
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    max_area = max(max_area, curr_area)
        return max_area