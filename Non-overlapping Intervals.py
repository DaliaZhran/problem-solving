# https://leetcode.com/problems/non-overlapping-intervals/

"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
"""
from typing import List

# Approach #1 Brute Force [Time Limit Exceeded]
# O(2^n) -> Total possible number of Combinations of subsets are 2^n


# Merge Intervals -> Greedy
"""
    if two intervals are overlapping, we want to remove the interval that has the longer end point -- the longer interval will always overlap with more or the same number of future intervals compared to the shorter one
"""
# Time: O(nlogn)
# Space: O(1)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= prev_end:  # no overlap
                prev_end = interval[1]
            elif interval[1] < prev_end:  # new interval overlaps and is smaller than prev interval so we remove the prev one
                count += 1
                prev_end = interval[1]
            else:
                count += 1
        return count


# greedy sol based on end points
"""
The heuristic is: always pick the interval with the earliest end time. Then you can get the maximal number of non-overlapping intervals. (or minimal number to remove).
This is because, the interval with the earliest end time produces the maximal capacity to hold rest intervals.
E.g. Suppose current earliest end time of the rest intervals is x. Then available time slot left for other intervals is [x:]. If we choose another interval with end time y, then available time slot would be [y:]. Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.

Therefore, we can sort interval by ending time and key track of current earliest end time. Once next interval's start time is earlier than current end time, then we have to remove one interval. Otherwise, we update earliest end time.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[-1])
        count = 1
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= prev_end:
                count += 1
                prev_end = interval[1]

        return len(intervals) - count
