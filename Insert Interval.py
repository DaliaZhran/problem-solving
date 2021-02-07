# https://leetcode.com/problems/insert-interval/

"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""

# Skip all non overlapping intervals, then merge, then add to result
# Time: O(N)
# Space: O(N)
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        start, end = 0, 1
        merged = []

        while i < len(intervals) and intervals[i][end] > newInterval[start]:
            merged.append(intervals[i])
            i += 1

        # newInterval[end] < intervals[i][start] means no overlapping
        while i < len(intervals) and newInterval[end] >= intervals[i][start]:
            newInterval = [min(intervals[i][start], newInterval[start]), max(intervals[i][end], newInterval[end])]
            # intervals.remove(intervals[i]) # -> this is not a good solution as remove takes O(n)
            i += 1

        merged.append(newInterval)
        # intervals.insert(i, newInterval)
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        # return intervals
        return merged


# Another Solution
# use a number line to explain it
# Time: O(N)
# Space: O(N)
def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left, right = [], []
    for i in intervals:
        if i.end < s:
            left.append(i)
        elif i.start > e:
            right.append(i)
        else:
            s = min(s, i.start)
            e = max(e, i.end)
    return left + [s, e] + right


## Scenario 1 -> non-overlapping -> left list
#                       |-------|           -> new interval
#    |----------------|                     -> current interval

## Scenario 2 -> non-overlapping -> right list
#         |-------|                         -> new interval
#                   |----------------|      -> current interval

## Scenario 3
#         |-------|         -> new interval
#    |----------------|     -> current interval

## Scenario 4
#     |-------|                 -> new interval
#        |----------------|     -> current interval

## Scenario 5
#                |-------|          -> new interval
#  |----------------|               -> current interval

# my implementation of the prev technique
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        start, end = 0, 1
        left, right = [], []

        s = newInterval[start]
        e = newInterval[end]
        for i in intervals:
            if i[end] < s:
                left.append(i)
            elif i[start] > e:
                right.append(i)
            else:
                s = min(i[start], s)
                e = max(i[end], e)

        return left + [[s, e]] + right