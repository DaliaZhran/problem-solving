# https://leetcode.com/problems/triangle/

"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
"""


# Brute Force -> Recursion
# Time: O(2^n) where n is len(triangle)
# Space: O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def solve(r, el_idx):
            if r == rows:
                return 0

            curr_sum = min(solve(r + 1, el_idx), solve(r + 1, el_idx + 1)) + triangle[r][el_idx]

            return curr_sum

        rows = len(triangle)
        return solve(0, 0)


# Recursion with Memoization
# Time: O(n * n/2) where n is len(triangle)
# Space: O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def solve(r, el_idx):
            if r == rows:
                return 0

            if dp[r][el_idx]:
                return dp[r][el_idx]

            curr_sum = min(solve(r + 1, el_idx), solve(r + 1, el_idx + 1)) + triangle[r][el_idx]
            dp[r][el_idx] = curr_sum

            return curr_sum

        rows = len(triangle)
        dp = [[None] * (i + 1) for i in range(rows)]
        return solve(0, 0)