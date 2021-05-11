# https://leetcode.com/problems/find-peak-element/

"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""
from typing import List


# Brute Force
# Time: O(N)
# Space: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return i
        return n - 1


# Binary Search
# Time: O(logN)
# Space: O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


"""
If the next number is larger than current, it show an increasing curve, then the peak must in the right half, else in the left half. Since we know there's a local peak for sure.
"""

# same as above but using right to compare - conditions
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l + 1) // 2
            if nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                l = mid
        return l


# recursive binary solution -> worse than iterative
"""
public class Solution {
    public int findPeakElement(int[] nums) {
        return search(nums, 0, nums.length - 1);
    }
    public int search(int[] nums, int l, int r) {
        if (l == r)
            return l;
        int mid = (l + r) / 2;
        if (nums[mid] > nums[mid + 1])
            return search(nums, l, mid);
        return search(nums, mid + 1, r);
    }
}
"""


# good expl -> https://leetcode.com/problems/find-peak-element/discuss/788474/General-Binary-Search-Thought-Process-%3A-4-Templates
