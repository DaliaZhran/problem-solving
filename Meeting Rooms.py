# https://leetcode.com/problems/meeting-rooms/

"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
"""

# * Approach 1: Brute Force
# Time : O(n^2)
# Space : O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if min(intervals[i][1], intervals[i][1]) > max(intervals[i][0], intervals[i][0]):
                    return False
        return True


# * Approach 2: Sorting
# Time : O(nlogn)
# Space : O(n)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort(key=lambda x: x[0])

        for interval in range(len(intervals) - 1):
            if intervals[interval][1] > intervals[interval + 1][0]:
                return False

        return True


# sorting by ends
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < prev_end:
                return False
            prev_end = interval[1]
        return True


# * Approach 3: A general solution that keeps also how many persons we need to attend all meetings/ number of rooms - more complicated though
# Time : O(nlogn)
# Space : O(n)
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        if not intervals:
            return True

        intervals.sort(key=lambda x: x[0])
        allocated_rooms = []
        heappush(allocated_rooms, intervals[0][1])

        for interval in intervals[1:]:
            if allocated_rooms[0] <= interval[0]:
                heappop(allocated_rooms)
            heappush(allocated_rooms, interval[1])

        return len(allocated_rooms) == 1
