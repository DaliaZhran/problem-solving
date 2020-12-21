# https://leetcode.com/problems/remove-covered-intervals/

"""
Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
"""

# Time complexity : O(NlogN) since the sorting dominates the complexity of the algorithm.

# Space complexity : O(N)

# The space complexity of the sorting algorithm depends on the implementation of each program language.

# For instance, the sorted() function in Python is implemented with the Timsort algorithm whose space complexity is O(N).

# In Java, the Arrays.sort() is implemented as a variant of quicksort algorithm whose space complexity is O(logN).
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        remaining = 0
        prev_end = 0
        for i in range(len(intervals)):
            if intervals[i][1] > prev_end:
                remaining += 1
                prev_end = intervals[i][1]

        return remaining
