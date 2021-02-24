# https://leetcode.com/problems/paint-house-ii/

"""There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.
"""


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
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