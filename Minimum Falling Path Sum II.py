# https://leetcode.com/problems/minimum-falling-path-sum-ii/

"""
Given a square grid of integers arr, a falling path with non-zero shifts is a choice of exactly one element from each row of arr, such that no two elements chosen in adjacent rows are in the same column.

Return the minimum sum of a falling path with non-zero shifts.
"""


# Recursion + Memoization
# Time: O(cols^rows)
# Space: O(rows)
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        def min_path(r, c):
            if r == rows:
                return 0

            value = arr[r][c]
            ans = float("inf")
            for j in range(cols):
                if j == c:
                    continue
                ans = min(ans, min_path(r + 1, j) + value)

            return ans

        rows = len(arr)
        cols = len(arr[0])
        min_sum = float("inf")

        for i in range(cols):
            min_sum = min(min_sum, min_path(0, i))
        return min_sum


# Recursion + Memoization
# Time: O(rows*cols)
# Space: O(rows*cols)
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        def min_path(r, c):
            if r == rows:
                return 0

            if dp[r][c] != -1:
                return dp[r][c]

            value = arr[r][c]
            ans = float("inf")
            for j in range(cols):
                if j == c:
                    continue
                ans = min(ans, min_path(r + 1, j) + value)

            dp[r][c] = ans
            return ans

        rows = len(arr)
        cols = len(arr[0])
        dp = [[-1] * cols for _ in range(rows)]
        min_sum = float("inf")

        for i in range(cols):
            min_sum = min(min_sum, min_path(0, i))
        return min_sum


import heapq

# Bottom Up - Iterative DP
# Time: O(rows*cols * cols * log(t)) -> cols * log(t) is complexity of nsmallest
# Space: O(1)
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        rows = len(arr)
        cols = len(arr[0])
        for i in range(1, rows):
            smallest = heapq.nsmallest(2, arr[i - 1])  # smallest 2 elements from prev col
            for j in range(cols):
                if arr[i - 1][j] == smallest[0]:
                    arr[i][j] += smallest[1]
                else:
                    arr[i][j] += smallest[0]

        return min(arr[-1])


# Same Idea but without heapq
# Time: O(rows*cols)
# Space: O(1)
class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        rows = len(arr)
        cols = len(arr[0])

        prv_row_min1 = prv_row_min2 = 0
        prev_pos1 = -1

        for i in range(rows):
            curr_row_min1 = curr_row_min2 = float("inf")
            for j in range(cols):
                if prev_pos1 != j:
                    min_val = prv_row_min1
                else:
                    min_val = prv_row_min2

                if min_val + arr[i][j] < curr_row_min1:
                    curr_row_min2 = curr_row_min1
                    curr_row_min1 = min_val + arr[i][j]
                    curr_pos = j
                else:
                    curr_row_min2 = min(curr_row_min2, min_val + arr[i][j])

            prv_row_min1, prv_row_min2 = curr_row_min1, curr_row_min2
            prev_pos1 = curr_pos

        return prv_row_min1


# Nice Implementation -> https://leetcode.com/problems/minimum-falling-path-sum-ii/discuss/451258/Simple-DP(Java)-Same-problem-as-Paint-House-2-(265)
