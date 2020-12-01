# https://leetcode.com/problems/median-of-two-sorted-arrays/

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
"""

from heapq import heappop, heappush


# time -> O(max(m, n , (m+n)/2))
# space -> O(m+n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        N = len(nums1) + len(nums2)
        heap_size = N // 2
        if N % 2:
            heap_size += 1

        min_heap = []
        for num in nums1:
            heappush(min_heap, num)

        for num in nums2:
            heappush(min_heap, num)

        k = heap_size - 1
        while min_heap:
            if k == 0:
                median = heappop(min_heap)
                if N % 2 == 0:
                    median += heappop(min_heap)
                    median /= 2.0
                return median
            heappop(min_heap)
            k -= 1


# better
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        size = (m + n) // 2 + 1

        q = []
        for i in nums1:
            heappush(q, i)
            if len(q) > size:
                heappop(q)

        for i in nums2:
            heappush(q, i)
            if len(q) > size:
                heappop(q)

        if (m + n) % 2 == 1:
            return heappop(q)
        else:
            med1 = heappop(q)
            med2 = heappop(q)
            return (med1 + med2) / 2.0


# check binary search and other solutions