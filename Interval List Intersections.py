# https://leetcode.com/problems/interval-list-intersections/

"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a < b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
"""
from typing import List


# Merge Intervals
# Time: O(n1 + n2)
# Space: O(n1 + n2) for res
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        n1, n2 = len(firstList), len(secondList)
        p1, p2 = 0, 0
        res = []
        while p1 < n1 and p2 < n2:
            if firstList[p1][1] < secondList[p2][0]:
                p1 += 1
            elif secondList[p2][1] < firstList[p1][0]:
                p2 += 1
            else:  # there is intersection
                start = max(firstList[p1][0], secondList[p2][0])
                end = min(firstList[p1][1], secondList[p2][1])
                res.append([start, end])
                if firstList[p1][1] > secondList[p2][1]:
                    p2 += 1
                elif firstList[p1][1] < secondList[p2][1]:
                    p1 += 1
                else:
                    p1 += 1
                    p2 += 1
        return res


# Shorter Implementation
# Time: O(n1 + n2)
# Space: O(n1 + n2) for res
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        n1, n2 = len(firstList), len(secondList)
        p1, p2 = 0, 0
        res = []
        while p1 < n1 and p2 < n2:
            start = max(firstList[p1][0], secondList[p2][0])
            end = min(firstList[p1][1], secondList[p2][1])
            if start <= end:  # if there is intersection, append it
                res.append([start, end])
            if firstList[p1][1] > secondList[p2][1]:
                p2 += 1
            else:
                p1 += 1
        return res


# Fastest implementation
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        n1, n2 = len(firstList), len(secondList)
        p1, p2 = 0, 0
        res = []
        while p1 < n1 and p2 < n2:
            start = max(firstList[p1][0], secondList[p2][0])
            end = min(firstList[p1][1], secondList[p2][1])
            if start <= end:
                res.append([start, end])
            if firstList[p1][1] > secondList[p2][1]:
                p2 += 1
            elif firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p1 += 1
                p2 += 1
        return res
