# https://leetcode.com/problems/find-k-closest-elements/solution/

"""
Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
"""


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        while l < r:
            mid = l + (r - l) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid
        return arr[l : l + k]
