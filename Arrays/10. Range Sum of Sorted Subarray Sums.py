# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

"""
Given the array nums consisting of n positive integers. You computed the sum of all non-empty continous subarrays from the array and then sort them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 10^9 + 7.

Example 1:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13 
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 
"""
from heapq import heappop, heappush

# Heap
# O(N^2 logN) worst time (but much faster on average) & O(N) space
class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        min_heap = []
        for i, v in enumerate(nums):
            heappush(min_heap, (v, i))

        res = 0
        for k in range(1, right + 1):
            x, i = heappop(min_heap)
            if k >= left:
                res += x
            if i + 1 < n:
                heappush(min_heap, (x + nums[i + 1], i + 1))
        return res % (pow(10, 9) + 7)


# Another Solution
# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/733047/Python-Binary-Search-Time-O(NlogSum(A))