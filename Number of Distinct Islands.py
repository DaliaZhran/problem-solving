# https://leetcode.com/problems/number-of-distinct-islands/

"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.
"""

# Approach 1: Brute Force -> get each island, then check if it is unique
# Time: O(M^2 * N^2)
# Space: O(M * N)
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def is_unique(curr_island):
            for other_island in unique_islands:
                if len(curr_island) != len(other_island):
                    continue
                for cell1, cell2 in zip(curr_island, other_island):
                    if cell1 != cell2:
                        break
                else:
                    return False
            return True

        def solve(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in seen or grid[r][c] == 0 or grid[r][c] == 0:
                return
            seen.add((r, c))
            curr_island.append((r - origin_row, c - origin_col))
            solve(r + 1, c)
            solve(r - 1, c)
            solve(r, c + 1)
            solve(r, c - 1)

        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        unique_islands = []
        for i in range(rows):
            for j in range(cols):
                curr_island = []
                origin_row = i
                origin_col = j
                solve(i, j)
                if curr_island and is_unique(curr_island):
                    unique_islands.append(curr_island)

        return len(unique_islands)


# Approach 2: Hash By Local Coordinates
# Use a set to keep track of unique sets instead of looping over all islands in a list
# Time: O(M * N)
# Space: O(M * N)
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def solve(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in seen or grid[r][c] == 0 or grid[r][c] == 0:
                return
            seen.add((r, c))
            curr_island.append((r - origin_row, c - origin_col))
            solve(r + 1, c)
            solve(r - 1, c)
            solve(r, c + 1)
            solve(r, c - 1)

        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        unique_islands = set()
        for i in range(rows):
            for j in range(cols):
                curr_island = []
                origin_row = i
                origin_col = j
                solve(i, j)
                # curr_island = [str(x) for x in curr_island]
                if curr_island:
                    # unique_islands.add(''.join(curr_island))
                    unique_islands.add(frozenset(curr_island))
                    # unique_islands.add(tuple(curr_island))

        return len(unique_islands)


# Approach 3: Hash By Path Signature
# Time: O(M * N)
# Space: O(M * N)
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def solve(r, c, path):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in seen or grid[r][c] == 0 or grid[r][c] == 0:
                return
            seen.add((r, c))
            curr_path.append(path)
            solve(r + 1, c, "D")
            solve(r - 1, c, "U")
            solve(r, c + 1, "R")
            solve(r, c - 1, "L")
            curr_path.append("0")

        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        unique_islands = set()
        for i in range(rows):
            for j in range(cols):
                curr_path = []
                solve(i, j, "0")
                if curr_path:
                    unique_islands.add(tuple(curr_path))

        return len(unique_islands)
