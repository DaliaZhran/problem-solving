# https://leetcode.com/problems/peak-index-in-a-mountain-array/

"""
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
"""


# Linear Scan
# Time: O(N)
# Space: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(1, len(arr)):
            if arr[i] > arr[i + 1]:
                return i


# Binary Search
# Time: O(log N)
# Space: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        start, end = 0, n - 1

        while start < end:
            mid = (start + end) // 2
            if arr[mid] >= arr[mid + 1]:
                end = mid
            else:
                start = mid + 1
        return start


# check difference in BS: https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/139840/JavaPython-3-O(n)-and-O(log(n))-codes


# just for knowledge -> https://leetcode.com/problems/peak-index-in-a-mountain-array/discuss/139848/C%2B%2BJavaPython-Better-than-Binary-Search