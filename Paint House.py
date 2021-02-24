# https://leetcode.com/problems/paint-house/

"""
There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.
"""


# DP Bottom Up
# Time: O(rows)
# Space: O(1)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        rows = len(costs)
        prev_row = costs[0]

        for i in range(1, rows):

            curr_row = costs[i]

            curr_row[0] += min(prev_row[1], prev_row[2])
            curr_row[1] += min(prev_row[0], prev_row[2])
            curr_row[2] += min(prev_row[0], prev_row[1])

            prev_row = curr_row

        return min(prev_row)


# General Code -> not stricted to 3 colors
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        rows = len(costs)
        cols = len(costs[0])

        prv_row_min1 = prv_row_min2 = 0
        prev_pos1 = -1

        for i in range(rows):
            curr_row_min1 = curr_row_min2 = float("inf")
            for j in range(cols):
                if prev_pos1 != j:
                    min_val = prv_row_min1
                else:
                    min_val = prv_row_min2

                if min_val + costs[i][j] < curr_row_min1:
                    curr_row_min2 = curr_row_min1
                    curr_row_min1 = min_val + costs[i][j]
                    curr_pos = j
                else:
                    curr_row_min2 = min(curr_row_min2, min_val + costs[i][j])

            prv_row_min1, prv_row_min2 = curr_row_min1, curr_row_min2
            prev_pos1 = curr_pos

        return prv_row_min1
