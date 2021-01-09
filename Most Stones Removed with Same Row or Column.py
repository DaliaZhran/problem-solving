# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

# DFS
# Time Complexity : O(n^2)
# Space Complexity : O(n)
# Idea -> removedStones = #stones - #connected_islands
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(curr_stone, visited):
            visited.add(tuple(curr_stone))
            for stone2 in stones:
                if tuple(stone2) not in visited:
                    if curr_stone[0] == stone2[0] or curr_stone[1] == stone2[1]:
                        dfs(stone2, visited)

        visited = set()
        count = 0
        for stone in stones:
            if tuple(stone) not in visited:
                dfs(stone, visited)
                count += 1
        return len(stones) - count
