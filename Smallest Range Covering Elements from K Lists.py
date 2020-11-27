# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

"""
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
"""
from heapq import heappop, heappush

# * the idea is to draw a number line for all lists and see how range shrinks
# time -> O(N log M)
# space -> O(M)
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        min_heap = []
        smallest_range = [0, float("inf")]
        curr_max_num = -float("inf")

        # put the 1st element of each array in the max heap
        for arr_index in range(len(nums)):
            heappush(min_heap, (nums[arr_index][0], 0, arr_index))
            curr_max_num = max(curr_max_num, nums[arr_index][0])

        while len(min_heap) == len(nums):
            num, i, arr_index = heappop(min_heap)
            if smallest_range[1] - smallest_range[0] > curr_max_num - num:
                smallest_range = [num, curr_max_num]

            if len(nums[arr_index]) > i + 1:
                # insert the next element in the heap
                heappush(min_heap, (nums[arr_index][i + 1], i + 1, arr_index))
                curr_max_num = max(curr_max_num, nums[arr_index][i + 1])

        return smallest_range


# check other solutions