# https://leetcode.com/problems/flood-fill/

"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.
"""

# DFS
# Time: O(rows * cols)
# Space: O(rows * cols)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def fill(r, c):
            if r < 0 or r == rows or c < 0 or c == cols:
                return
            if image[r][c] != color:
                return
            image[r][c] = newColor
            fill(r + 1, c)
            fill(r - 1, c)
            fill(r, c + 1)
            fill(r, c - 1)

        rows = len(image)
        cols = len(image[0])
        color = image[sr][sc]
        if newColor == color:
            return image
        fill(sr, sc)
        return image