# https://leetcode.com/problems/sort-colors/solution/

"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
from typing import List


# idea -> sort 0s on beginning and sort 2s at the end and then 1s in turn will be sorted
# time -> O(n)
# space -> O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # return nums.sort()
        i, p0, p2 = 0, 0, len(nums) - 1  # i -> iterator, p0 -> count of 0s, p2 -> count of 2s

        while i <= p2:  # they cover all cases -> we always move one of them
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                i += 1
                p0 += 1
            elif nums[i] == 1:
                # ignore 1s until we find 0s, we will swap it with 0
                i += 1
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
                # we cannot be sure that nums[p2] is 0 or 1 so we just keep the i pointer as it is

        return nums


# two pass O(m+n) space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0, c1, c2 = 0, 0, 0
        for num in nums:
            if num == 0:
                c0 += 1
            elif num == 1:
                c1 += 1
            else:
                c2 += 1

        for i in range(c0):
            nums[i] = 0
        for i in range(c1):
            nums[c0 + i] = 1
        for i in range(c2):
            nums[c0 + c1 + i] = 2


# one pass in place solution
"""
void sortColors(int A[], int n) {
    int n0 = -1, n1 = -1, n2 = -1;
    for (int i = 0; i < n; ++i) {
        if (A[i] == 0)
        {
            A[++n2] = 2; A[++n1] = 1; A[++n0] = 0;
        }
        else if (A[i] == 1)
        {
            A[++n2] = 2; A[++n1] = 1;
        }
        else if (A[i] == 2)
        {
            A[++n2] = 2;
        }
    }
}
"""

# https://leetcode.com/problems/sort-colors/discuss/26500/Four-different-solutions
