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

        while i < len(intervals) and newInterval[start] > intervals[i][end]:
            merged.append(intervals[i])
            i += 1

        while i < len(intervals) and newInterval[end] >= intervals[i][start]:
            newInterval = [min(intervals[i][start], newInterval[start]), max(
                intervals[i][end], newInterval[end])]
            # intervals.remove(intervals[i]) # -> this is not a good solution as remove takes O(n)
            i += 1

        merged.append(newInterval)
        # intervals.insert(i, newInterval)
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        # return intervals
        return merged


''' Another Solution '''


def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left, right = [], []
    for i in intervals:
        if i.end < s:
            left += i,
        elif i.start > e:
            right += i,
        else:
            s = min(s, i.start)
            e = max(e, i.end)
    return left + [s, e] + right
