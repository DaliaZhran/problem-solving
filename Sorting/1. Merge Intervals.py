# https://leetcode.com/problems/merge-intervals/

# Given a collection of intervals, merge all overlapping intervals.
# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


# * time -> O(n)
# * space -> O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals:
            if i[0] > end:
                res.append([start, end])
                start = i[0]
                end = i[1]
            else:
                if i[1] > end:
                    end = i[1]
        res.append([start, end])
        return res