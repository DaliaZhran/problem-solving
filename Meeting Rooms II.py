# https://leetcode.com/problems/meeting-rooms-ii/

"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
"""

from collections import defaultdict
from heapq import heappop, heappush


# * Approach 1: Heap
# TIme -> O(NlogN)
# Space -> O(N)
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        allocated_rooms = []
        heappush(allocated_rooms, intervals[0][1])

        for interval in intervals[1:]:
            if allocated_rooms[0] <= interval[0]:
                heappop(allocated_rooms)
            heappush(allocated_rooms, interval[1])

        return len(allocated_rooms)


# * Approach 2: Chronological Ordering
# TIme -> O(NlogN)
# Space -> O(N)
class Solution:
    def minMeetingRooms(self, intervals):

        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1
            start_pointer += 1

        return used_rooms


# Approach 1 is better since we are just sorting once and only creating one heap and it would be better if we have incoming times (stream)


# Using Map
# Time : O(NlogN)
# Space : O(N)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        mp = defaultdict(int)
        for interval in intervals:
            mp[interval[0]] += 1
            mp[interval[1]] -= 1

        rooms = 0
        max_needed = 0
        for k in sorted(mp.keys()):
            max_needed = max(max_needed, rooms)
            rooms += mp[k]

        return max_needed

# https://leetcode.com/problems/meeting-rooms-ii/discuss/203658/HashMapTreeMap-resolves-Scheduling-Problem