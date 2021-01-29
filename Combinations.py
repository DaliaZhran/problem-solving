# https://leetcode.com/problems/combinations/
# Note : Combinations -> Pascal's Triangle

"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""


# Backtracking
# Time: O(k * kCN)
# Space: O(kCN)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(choice, path):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(choice, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        res = []
        backtrack(1, [])
        return res


# More pruning for the search space -> first possible num for combination is n - k + 1
# Time: O(k * kCN)
# Space: O(kCN)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(choice, path, curr_k):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(choice, n - curr_k + 2):
                path.append(i)
                backtrack(i + 1, path, curr_k - 1)
                path.pop()

        res = []
        backtrack(1, [], k)
        return res


# https://leetcode.com/problems/combinations/discuss/26992/Short-Iterative-C%2B%2B-Answer-8ms