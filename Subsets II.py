# https://leetcode.com/problems/subsets-ii/

"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(path, index):
            if len(path) == k:
                res.add(tuple(path))
                return

            for i in range(index, n):
                path.append(nums[i])
                helper(path, i + 1)
                path.pop()

        n = len(nums)
        res = set()
        nums.sort()
        for k in range(n + 1):
            helper([], 0)
        return res


# Better Implementation
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(path, index):
            res.append(list(path))
            for i in range(index, n):
                if i == index or nums[i] != nums[i - 1]:
                    path.append(nums[i])
                    helper(path, i + 1)
                    path.pop()

        n = len(nums)
        res = []
        nums.sort()
        helper([], 0)
        return res
