# https://leetcode.com/problems/find-the-duplicate-number/
"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
 
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
"""

# How can we prove that at least one duplicate number must exist in nums? if the sum != n(n+1)/2 or xor of numbers and their order does not equal to 0

# * Brute Force
# time -> O(n^2)
# space -> O(1)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i != j and n1 == n2:
                    return n1


# * Sorting
# time -> O(nlogn)
# space -> O(n) for sorting
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]


# * Modifying the array
# time -> O(n)
# space -> O(1)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        for i in range(len(nums)):
            if nums[abs(nums[i])] > 0:
                nums[abs(nums[i])] *= -1
            else:
                return abs(nums[i])


# * Set
# time -> O(n)
# space -> O(n)
class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


# * find cycle
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        temp = nums[nums[fast]]
        length = 1
        while temp != nums[fast]:
            temp = nums[temp]
            length += 1

        slow, fast = nums[0], nums[0]
        while length > 0:
            length -= 1
            fast = nums[fast]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


# * hare and tortiose algorithm - cycle detection
# time -> O(n)
# space -> O(1)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[nums[0]], nums[nums[nums[0]]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


# check binary search solution
# https://leetcode.com/problems/find-the-duplicate-number/discuss/72844/Two-Solutions-(with-explanation)%3A-O(nlog(n))-and-O(n)-time-O(1)-space-without-changing-the-input-array