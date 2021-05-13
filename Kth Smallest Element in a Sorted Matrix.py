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
from heapq import heapify, heappop, heappush
from typing import List


# Using Heap
# time: O((n^2)log(n^2))
# space: O(n^2)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(n):
            for j in range(n):
                heappush(heap, matrix[i][j])

        while heap and k:
            last = heappop(heap)
            k -= 1
        return last


# Using Heap
# time: O((n)log(n))
# space: O(n)
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(min(k, n)):
            heap.append((matrix[i][0], 0, i))

        heapify(heap)  # -> in python, it takes O(n)

        while k:
            num, col, row = heappop(heap)
            if col + 1 < n:
                heappush(heap, (matrix[row][col + 1], col + 1, row))
            k -= 1
        return num


# check binary solution -> https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/

# time: O(N log(M - N))
# Space: O(1)
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        start, end = matrix[0][0], matrix[n - 1][n - 1]

        while start < end:
            mid = start + (end - start) // 2
            smaller, larger = matrix[0][0], matrix[n - 1][n - 1]
            count, smaller, larger = self.countLessEqual(matrix, smaller, mid, larger)

            if count == k:
                return smaller
            elif count > k:
                end = smaller
            else:
                start = larger

        return start

    def countLessEqual(self, matrix, smaller, mid, larger):
        count, n = 0, len(matrix)
        row, col = n - 1, 0

        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                # As matrix[row][col] is bigger than the mid, let's keep track of the
                # smallest number greater than the mid
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                # As matrix[row][col] is less than or equal to the mid, let's keep track of the
                # biggest number less than or equal to the mid
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1

        return count, smaller, larger
