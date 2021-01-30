# https://leetcode.com/problems/permutations/

"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

# Backtracking
# Intially, we have N options, then N-1 then N-2 so N * (N-1) * (N-2) .. -> N!
# Time: O(N*N!) -> O(N!) .. also nPn == n!
# Space: O(N*N!) -> O(N!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_len, curr_permutation):
            if target_len == curr_len:
                res.append(curr_permutation[:])

            for num in nums:
                if num in curr_permutation:
                    continue
                curr_permutation.append(num)
                backtrack(curr_len + 1, curr_permutation)
                curr_permutation.pop()

        res = []
        target_len = len(nums)
        backtrack(0, [])
        return res


# pythonic short way
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_nums, path):
            if not curr_nums:
                res.append(path)

            for i in range(len(curr_nums)):
                backtrack(curr_nums[:i] + curr_nums[i + 1 :], path + [curr_nums[i]])

        res = []
        backtrack(nums, [])
        return res