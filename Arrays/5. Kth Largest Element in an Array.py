# https://leetcode.com/problems/kth-largest-element-in-an-array/

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
"""


from heapq import *

# time -> O(N * log k)
# space -> O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for i in range(k):
            heappush(max_heap, nums[i])

        for i in range(k, len(nums)):
            if max_heap[0] < nums[i]:
                heappop(max_heap)
                heappush(max_heap, nums[i])

        return max_heap[0]
