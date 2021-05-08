# https://leetcode.com/problems/sliding-window-maximum/

"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

# Sliding Window with calculating max each time
# Time: O(n^2) -> TLE
# Space: O(1)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []

        n = len(nums)
        if n <= k:
            return [max(nums)]

        res = [max(nums[:k])]
        start = 0
        for end in range(k, n):
            if end - start + 1 > k:
                start += 1
            res.append(max(nums[start : end + 1]))
        return res


from heapq import heappop, heappush
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []

        n = len(nums)
        if n <= k:
            return [max(nums)]

        res = []
        heap = []
        start = 0

        for end in range(n):
            heappush(heap, (-nums[end], end))
            if end - start + 1 > k:
                start += 1

            while heap and heap[0][1] < start:
                heappop(heap)

            if end - start + 1 == k:
                res.append(-heap[0][0])

        return res
