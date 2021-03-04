# https://leetcode.com/problems/subsets/

"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

# Backtracking
# this is like BFS for the recursion tree
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(path, index):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(index, n):
                path.append(nums[i])
                helper(path, i + 1)
                path.pop()

        n = len(nums)
        res = []
        for k in range(n + 1):
            helper([], 0)
        return res


# better implementation'
# this is like DFS for the recursion tree
# Time: 2^N
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(path, index):
            res.append(list(path))
            for i in range(index, n):
                path.append(nums[i])
                helper(path, i + 1)
                path.pop()

        n = len(nums)
        res = []
        helper([], 0)
        return res
