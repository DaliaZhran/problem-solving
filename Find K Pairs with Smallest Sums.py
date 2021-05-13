# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
"""
from heapq import heappop, heappush
from typing import List


# Brute Force
# Time: O(nm)
# space: O(nm)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        sums = []
        for i in range(n):
            for j in range(m):
                sums.append((nums1[i] + nums2[j], nums1[i], nums2[j]))

        sums.sort()
        return [[el1, el2] for s, el1, el2 in sums[:k]]


# Time: O(min(n,k) * m * logk)
# space: O(k)
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        heap = []
        for i in range(min(n, k)):
            for j in range(m):
                summ = nums1[i] + nums2[j]
                heappush(heap, (-summ, nums1[i], nums2[j]))
                if len(heap) > k:
                    heappop(heap)

        res = []
        while heap:
            _, el1, el2 = heappop(heap)
            res.append([el1, el2])

        return res


# check other solutions -> https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation
