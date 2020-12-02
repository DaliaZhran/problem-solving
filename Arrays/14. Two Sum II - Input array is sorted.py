# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

# time -> O(n)
# space -> O(1)
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1


# dictionary
# time -> O(n)
# space -> O(n)
def twoSum2(self, numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target - num in dic:
            return [dic[target - num] + 1, i + 1]
        dic[num] = i


# binary search
# time -> O(N log N)
# space = O(1)
def twoSum(self, numbers, target):
    for i in xrange(len(numbers)):
        l, r = i + 1, len(numbers) - 1
        tmp = target - numbers[i]
        while l <= r:
            mid = l + (r - l) // 2
            if numbers[mid] == tmp:
                return [i + 1, mid + 1]
            elif numbers[mid] < tmp:
                l = mid + 1
            else:
                r = mid - 1
