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


# Heap
# time -> O(max(m, n , (m+n)/2))
# space -> O(m+n)
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        heap = []
        for n in nums1:
            heappush(heap, n)

        for n in nums2:
            heappush(heap, n)

        total_len = len(heap)
        if total_len == 1:
            return heappop(heap)

        for i in range(total_len // 2 - 1):
            heappop(heap)

        if total_len % 2:
            heappop(heap)
            return heappop(heap)
        else:
            return (heappop(heap) + heappop(heap)) / 2.0


# Heap -> faster
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


# Binary Search
# https://medium.com/@hazemu/finding-the-median-of-2-sorted-arrays-in-logarithmic-time-1d3f2ecbeb46
# Time: O(log(min(m, n)))
# Space: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        # to decrease the binary search time, do it on the smaller one
        # we always choose nums1 to be the smaller array
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        if len2 == 0:
            return -1

        split1_min, split1_max = 0, len1
        half = (len1 + len2 + 1) // 2

        while split1_min <= split1_max:
            split1 = (split1_min + split1_max + 1) // 2  # index that splits nums1
            split2 = half - split1

            if split1 < len1 and nums2[split2 - 1] > nums1[split1]:
                split1_min = split1 + 1
            elif split1 > 0 and nums1[split1 - 1] > nums2[split2]:
                split1_max = split1 - 1

            else:
                if split1 == 0:
                    max_left = nums2[split2 - 1]
                elif split2 == 0:
                    max_left = nums1[split1 - 1]
                else:
                    max_left = max(nums1[split1 - 1], nums2[split2 - 1])

                if (len1 + len2) % 2 == 1:
                    return max_left

                if split1 == len1:
                    min_right = nums2[split2]
                elif split2 == len2:
                    min_right = nums1[split1]
                else:
                    min_right = min(nums1[split1], nums2[split2])

                return (max_left + min_right) / 2.0


# check this -> https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation