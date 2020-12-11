# https://leetcode.com/problems/merge-intervals/

# Given a collection of intervals, merge all overlapping intervals.
# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


# * time -> O(n)
# * space -> O(n)
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                if intervals[i][1] > end:
                    end = intervals[i][1]
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        res.append([start, end])
        return res
