# https://leetcode.com/problems/check-if-it-is-a-straight-line/

"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
"""


# to avoid division by 0 -> instead of calculating the slope, do cross multiplication between 2 slopes
# Time: O(n)
# Space: O(1)
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        x0, y0 = coordinates[0][0], coordinates[0][1]

        x_diff = coordinates[1][0] - x0
        y_diff = coordinates[1][1] - y0
        for x, y in coordinates:
            if y_diff * (x - x0) != x_diff * (y - y0):
                return False

        return True
