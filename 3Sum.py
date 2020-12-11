# https://leetcode.com/problems/3sum/

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

"""

# time -> O(n^2)
# space =  from O(log n) to O(n), depending on the implementation of the sorting algorithm and ignoring the space of the output
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
                break  # since the array is sorted, there would be no -ve number in the next part and thus no triplets == 0
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


# time -> O(n^2)
# space =  from O(n) due to the hashset
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
                break  # since the array is sorted, there would be no -ve number in the next part and thus no triplets == 0
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


# Approach 3: "No-Sort" solution
# time -> O(n^2)
# space =  from O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i + 1 :]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res