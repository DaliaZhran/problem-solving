# https://leetcode.com/problems/majority-element-ii/

"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Follow-up: Could you solve the problem in linear time and in O(1) space?

 

Example 1:

Input: nums = [3,2,3]
Output: [3]
"""

# * Brute Force
# Time -> O(n^2) -> Time limit exceeded
# Space -> O(1) ignoring the output
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set()
        majority_count = len(nums) // 3
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                res.add(num)

        return list(res)


# * Hashmap
# Time -> O(n)
# Space -> O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        count = Counter(nums)
        n = len(nums)
        for num, freq in count.items():
            if freq > n // 3:
                res.append(num)
        return res


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        n = len(nums)
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        res = set()
        for c in [candidate1, candidate2]:
            if nums.count(c) > n // 3:
                res.add(c)

        return list(res)
