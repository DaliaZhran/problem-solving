# https://leetcode.com/problems/3sum/

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

"""
# * Approach 1: Brute Force -> O(n^3) solution


# * Approach 2: Two pointers
# time -> O(n^2)
# space = O(n), due to sorting and ignoring the space of the output
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break  # since the array is sorted, there would be no -ve number in the next part and thus num of triplets = 0
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, result)
        return result

    def twoSum(self, nums, i, result):
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = nums[l] + nums[r] + nums[i]
            if sum == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            elif sum < 0:
                l += 1
            else:
                r -= 1


# * Approach 3: Hashset
# This approach will work too if the sum is not necessarily equal to the target, like in 3Sum Smaller and 3Sum Closest.
# time -> O(n^2)
# space ->  O(n) due to the hashset
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break  # since the array is sorted, there would be no -ve number in the next part and thus num of triplets = 0
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, result)
        return result

    def twoSum(self, nums, i, result):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                result.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1


# * Approach 3: "No-Sort"
# What if you cannot modify the input array, and you want to avoid copying it due to memory constraints?
# time -> O(n^2)
# space -> O(n) for the hashset/hashmap.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result, duplicates = set(), set()
        complements = {}

        for i in range(len(nums)):
            if nums[i] not in duplicates:
                duplicates.add(nums[i])  # to avoid doing the same search twice (avoid duplicates in the outer loop)
                for j in range(i + 1, len(nums)):
                    complement = -nums[i] - nums[j]
                    if complement in complements and complements[complement] == i:  # complements[complement] == i is used to make sure we encountered the complement in the current search iteration so we avoid getting the same index twice
                        result.add(tuple(sorted([nums[i], nums[j], complement])))

                    complements[nums[j]] = i
        return result