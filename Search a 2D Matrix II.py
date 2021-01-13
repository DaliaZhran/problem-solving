# https://leetcode.com/problems/search-a-2d-matrix-ii/

# Brute Force
# Time : O(mn)
# Space : O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target in row:
                return True

        return False


# Binary Search on diagonal
# Time : O(log(n!))
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)

            if vertical_found or horizontal_found:
                return True

    def binary_search(self, matrix, target, start, vertical):
        lo = start
        if vertical:
            hi = len(matrix) - 1
        else:
            hi = len(matrix[0]) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if not vertical:
                if matrix[start][mid] == target:
                    return True
                elif matrix[start][mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if matrix[mid][start] == target:
                    return True
                elif matrix[mid][start] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False


# Search Space Reduction
# Time : O(n+m)
# Space : O(1)
"""
i. if we start at bottom left corner => we can go right to get elements in increasing order & top to get elements in decreasing order.
ii. if we start at top right corner => we can go left to get elements in decreasing order & bottom to get elements in increasing order.
We can't have both choices if we start at top left or bottom right indices.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        if height == 0:
            return False
        width = len(matrix[0])

        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True

        return False