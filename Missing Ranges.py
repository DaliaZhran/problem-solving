# https://leetcode.com/problems/missing-ranges/

"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
"""

# Time -> O(N)
# space -> O(N) if we take the output into account and O(1) otherwise, where N is the length of the input array. This is because we could have a missing range between each of the consecutive element of the input array. Hence, our output list that we need to return will be of size N.
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        def formatRange(lower, upper):
            if lower == upper:
                return str(lower)
            return str(lower) + "->" + str(upper)

        n = len(nums)
        missing_ranges = []
        if n == 0:
            missing_ranges.append(formatRange(lower, upper))
            return missing_ranges

        # missing range at the beginning
        if lower < nums[0]:
            missing_ranges.append(formatRange(lower, nums[0] - 1))

        # missing ranges between elements
        for i in range(1, n):
            if nums[i] - nums[i - 1] > 1:
                missing_ranges.append(formatRange(nums[i - 1] + 1, nums[i] - 1))

        # missing range at the end
        if nums[n - 1] < upper:
            missing_ranges.append(formatRange(nums[n - 1] + 1, upper))

        return missing_ranges


# Another implementation (general if condition instead of dividing the problem into parts)
def findMissingRanges(self, A, lower, upper):
    result = []
    A.append(upper + 1)
    pre = lower - 1
    for i in A:
        if i == pre + 2:  # only one number missing in between
            result.append(str(i - 1))
        elif i > pre + 2:
            result.append(str(pre + 1) + "->" + str(i - 1))
        pre = i
    return result
