# https://leetcode.com/problems/minimum-time-difference/

"""
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
"""


# Brute Force [TLE]
# Time: O(n^2)
# Space: O(1)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        min_diff = 2000  # max difference is 1440
        for i in range(n):
            for j in range(i + 1, n):
                t1_h, t1_m = int(timePoints[i][:2]), int(timePoints[i][3:])
                t2_h, t2_m = int(timePoints[j][:2]), int(timePoints[j][3:])
                point1 = t1_h * 60 + t1_m
                point2 = t2_h * 60 + t2_m
                # there are 2 differences between each 2 points so we need to take the smallest one
                # There are two possible time differences between two time points.
                # e.g. from 1:00 to 2:00, time difference is 1 hour
                # e.g. from 2:00 to 1:00, time difference is 23 hours
                diff1 = abs(point2 - point1)
                diff2 = 1440 - diff1
                min_diff = min(min_diff, diff1, diff2)

        return min_diff


# Thinking Process -> https://leetcode.com/problems/minimum-time-difference/discuss/437793/Thinking-Process
# Time: O(n)
# Space: O(1)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        mark = [0] * 1440
        for t in timePoints:
            t_minutes = int(t[:2]) * 60 + int(t[3:])
            if mark[t_minutes]:
                return 0
            mark[t_minutes] = 1

        min_diff = 2000
        smallest_num, largest_num_so_far = -1, -1
        for minute, flag in enumerate(mark):
            if flag:
                if largest_num_so_far != -1:
                    min_diff = min(min_diff, minute - largest_num_so_far)

                largest_num_so_far = minute

                if smallest_num == -1:
                    smallest_num = minute

        # check the 2 differences of the smallest and largest time points
        diff1 = largest_num_so_far - smallest_num
        return min(min_diff, diff1, 1440 - diff1)


# Good Idea to subtract consecutive elements in array (shift by 1)
# (y - x) % (24 * 60) for x, y in zip(minutes, minutes[1:] + minutes[:1])