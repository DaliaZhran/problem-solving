# https://leetcode.com/problems/rotate-image/

"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

# * Approach 1: Transpose and then reverse
# * Rotation Clockwise
# first reverse up to down, then swap the symmetry
# 1 2 3     7 8 9     7 4 1
# 4 5 6  => 4 5 6  => 8 5 2
# 7 8 9     1 2 3     9 6 3

# Time complexity : (N^2)
# Space complexity : O(1) since we do a rotation in place.
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        for i in range(n):
            for j in range(n - 1, i - 1, -1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse the rows
        for i in range(n):
            matrix[i] = reversed(matrix[i])

        # reversing rows
        # for row in matrix:
        #     for i in range(n//2):
        #     row[i], row[~i] = row[~i], row[i]

        return matrix


# * Rotation Anti-Clockwise
# first reverse left to right, then swap the symmetry
# 1 2 3     3 2 1     3 6 9
# 4 5 6  => 6 5 4  => 2 5 8
# 7 8 9     9 8 7     1 4 7

# Time complexity : (N^2)
# Space complexity : O(1) since we do a rotation in place
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse columns
        for i in range(n / 2):
            for col in range(n):
                matrix[i][col], matrix[~i][col] = matrix[~i][col], matrix[i][col]

        return matrix