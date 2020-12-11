# https://leetcode.com/problems/top-k-frequent-elements/

"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

from heapq import *


class Solution:
    def topKFrequent(self, nums, k):
        freq_map = {}
        for val in nums:
            freq_map[val] = freq_map.get(val, 0) + 1

        min_heap = []
        for val in freq_map:
            heappush(min_heap, (freq_map[val], val))
            if len(min_heap) > k:
                heappop(min_heap)  # remove the smallest number so at the end we have only the largest k frequencies
        return [x[1] for x in min_heap]


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
