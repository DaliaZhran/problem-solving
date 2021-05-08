# https://leetcode.com/problems/top-k-frequent-elements/

"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
from collections import Counter
from heapq import *


# Heap
# Time: O(nlogk)
# Space: O(n + k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)

        min_heap = []
        for val in freq_map:
            heappush(min_heap, (freq_map[val], val))
            if len(min_heap) > k:
                heappop(min_heap)

        return [x[1] for x in min_heap]


# Approach 2: Quickselect (Hoare's selection algorithm)
