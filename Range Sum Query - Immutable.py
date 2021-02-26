# https://leetcode.com/problems/range-sum-query-immutable/

"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]
"""


# Brute Force
# Time: O(n) time per query, O(1) time pre-computation
# Space: O(1)
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        range_sum = 0
        for idx in range(i, j + 1):
            range_sum += self.nums[idx]
        return range_sum


# Use DP to store all sum ranges -> TLE
# Time: O(1) time per query, O(n^2) time pre-computation. The pre-computation done in the constructor takes O(n^2) time.
# Space: O(n^2)
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(nums)
        self.dp = [[0] * n for _ in range(n)]  # we can use a map instead to save space but it will be TLE too
        for i in range(0, n):
            self.dp[i][i] = nums[i]
            for j in range(i + 1, n):
                self.dp[i][j] = self.dp[i][j - 1] + nums[j]

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[i][j]


# Caching -> prefix sums
# Time: O(1) time per query, O(n) time pre-computation
# Space: O(n)
class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix_sum = [0] * (n + 1)
        for i in range(n):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sum[j + 1] - self.prefix_sum[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)