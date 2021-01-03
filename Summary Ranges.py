# https://leetcode.com/problems/summary-ranges/

"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""

# Time -> O(N)
# space -> O(N) if we take the output into account and O(1) otherwise, where N is the length of the input array. This is because we could have a missing range between each of the consecutive element of the input array. Hence, our output list that we need to return will be of size N.
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        summary_ranges = []
        n = len(nums)
        start = 0
        for end in range(n):
            if end + 1 < n and nums[end] + 1 == nums[end + 1]:
                continue
            if start == end:
                summary_ranges.append(str(nums[start]))
            else:
                summary_ranges.append(str(nums[start]) + "->" + str(nums[end]))
            start = end + 1
        return summary_ranges
