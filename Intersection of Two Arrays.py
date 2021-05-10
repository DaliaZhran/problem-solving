# https://leetcode.com/problems/intersection-of-two-arrays/

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""
from typing import List

# approach 1: brute force

# Two Sets
# Time: O(m + n)
# Space: O(m + n)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# Two pointers
# Time: O(m + n)
# Space: O(1)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        n1, n2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        res = []

        while p1 < n1 and p2 < n2:
            el1 = nums1[p1]
            el2 = nums2[p2]
            if el1 == el2:  # intersection
                res.append(el1)
                while p1 < n1 and nums1[p1] == el1:
                    p1 += 1
                while p2 < n2 and nums2[p2] == el2:
                    p2 += 1
            elif el1 < el2:
                while p1 < n1 and nums1[p1] == el1:
                    p1 += 1
            else:
                while p2 < n2 and nums2[p2] == el2:
                    p2 += 1

        return res
