# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
from heapq import heappush, heappop


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        N = len(matrix[0]) if matrix else 0
        min_heap = []
        for row in range(len(matrix)):
            heappush(min_heap, (matrix[row][0], 0, row))

        curr_count = curr_num = 0
        while min_heap:
            curr_num, col, row = heappop(min_heap)
            curr_count += 1
            if curr_count == k:
                break
            if col + 1 < N:
                heappush(min_heap, (matrix[row][col + 1], col + 1, row))

        return curr_num


# check binary solution -> https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/