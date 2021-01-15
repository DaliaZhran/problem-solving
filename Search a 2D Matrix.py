# https://leetcode.com/problems/search-a-2d-matrix/

# Binary Search
# Time : O(log(cols*rows))
# Space : O(1)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        start, end = 0, len(matrix[0])
        row = -1
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                row = i
                break
        if row == -1:
            return False

        while start <= end:
            mid = (start + end) >> 1
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False


# better sol
# Binary Search
# Time : O(log(cols*rows))
# Space : O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            element = matrix[mid // n][mid % n]
            if element == target:
                return True
            if element < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
