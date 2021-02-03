# https://leetcode.com/problems/android-unlock-patterns/


# Backtracking
# Time: O(n!)
# Space: O(n)
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def count_ways(curr, remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1

            visited[curr] = 1
            curr_res = 0
            for candidate in range(1, 10):
                if not visited[candidate] and (skip[curr][candidate] == 0 or visited[skip[curr][candidate]]):
                    curr_res += count_ways(candidate, remain - 1)
            visited[curr] = 0
            return curr_res

        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
        visited = [0] * 10
        res = 0
        for i in range(m, n + 1):
            res += count_ways(1, i - 1) * 4
            res += count_ways(2, i - 1) * 4
            res += count_ways(5, i - 1)

        return res


# Time: O(n!)
# Space: O(n)
class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def count_ways(curr, length, count):
            if length >= m:
                count += 1
            length += 1
            if length > n:
                return count

            visited[curr] = 1
            for candidate in range(1, 10):
                obstacle = skip[curr][candidate]
                if not visited[candidate] and (obstacle == 0 or visited[obstacle]):
                    count = count_ways(candidate, length, count)
            visited[curr] = 0
            return count

        skip = [[0] * 10 for _ in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
        visited = [0] * 10
        res = 0

        res += count_ways(1, 1, 0) * 4
        res += count_ways(2, 1, 0) * 4
        res += count_ways(5, 1, 0)

        return res
