# https://leetcode.com/problems/majority-element/

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

# * Brute Force
# Time -> O(n^2)
# Space -> O(1)
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num


# * Hashmap
# Time -> O(n)
# Space -> O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        n = len(nums)
        for num, freq in count.items():
            if freq > n // 2:
                return num


# * Sorting
# Time -> O(nlogn)
# Space -> O(1)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]


# * Boyer-Moore Voting Algorithm
# Time -> O(n)
# Space -> O(1)
# Note -> in this problem, it is guaranteed that there is a majority element. If it is not, then we need to verify the candidate frequence > N//2
# it depends on the fact that the number of the majority element mush be larger than all other elements combined.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# https://leetcode.com/problems/majority-element-ii/discuss/63520/boyer-moore-majority-vote-algorithm-and-my-elaboration