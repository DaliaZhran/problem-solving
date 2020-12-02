#   https://leetcode.com/problems/3sum-closest/

'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
''''


# time -> O(n^2)
# space =  from O(log n) to O(n), depending on the implementation of the sorting algorithm and ignoring the space of the output
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):  # -2 because the last 2 elements should be investigated with all other element + we want triplets
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == target:
                    return sum
                if abs(target - sum) < abs(target - result):
                    result = sum

                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1

        return result


'''
If an interviewer asks you whether you can achieve O(1) memory complexity, you can use the selection sort instead of a built-in sort in the Two Pointers approach. It will make it a bit slower, though the overall time complexity will be still O(n^2).
'''
