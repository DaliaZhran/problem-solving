# https://leetcode.com/problems/maximum-product-subarray/

"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums:
        #     return -float("inf")
        # if len(nums) == 1:
        #     return nums[0]

        start, end = 0, 0
        max_product = -float("inf")
        curr_window_product = 1

        while end < len(nums):
            if nums[end] == 0 and curr_window_product < 0 and start < end - 1:
                curr_window_product = curr_window_product // nums[start]
                start = start + 1
                max_product = max(curr_window_product, max_product)
            elif nums[end] == 0:
                max_product = max(0, max_product)
                curr_window_product = 1
                start = end + 1
                end += 1
            else:
                curr_window_product *= nums[end]
                end += 1
                max_product = max(curr_window_product, max_product)

        while start < end - 1 and curr_window_product < 0:
            curr_window_product = curr_window_product // nums[start]
            max_product = max(curr_window_product, max_product)
            start += 1

        return max_product


# https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity
# https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple
# https://leetcode.com/problems/maximum-product-subarray/discuss/48276/Python-solution-with-detailed-explanation