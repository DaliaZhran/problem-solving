# https://leetcode.com/problems/meeting-scheduler/

"""
Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

It is guaranteed that no two availability slots of the same person intersect with each other. That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

 

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]
"""

# Two Pointers
# Time : O(NlogN) + O(M+N)
# Space : O(1)
# we need the intersection to be duration or more
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        s1, s2 = 0, 0
        while s1 < len(slots1) and s2 < len(slots2):
            mutual_start = max(slots1[s1][0], slots2[s2][0])
            mutual_end = min(slots1[s1][1], slots2[s2][1])

            if mutual_start + duration <= mutual_end:
                return [mutual_start, mutual_start + duration]

            if mutual_end == slots1[s1][1]:
                s1 += 1
            else:
                s2 += 1

        return []


# Heap Solution
# https://leetcode.com/problems/meeting-scheduler/discuss/408506/JavaPython-3-simple-code-using-PriorityQueueheapq-w-brief-explanation-and-analysis