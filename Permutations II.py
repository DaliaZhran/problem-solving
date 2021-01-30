# https://leetcode.com/problems/permutations-ii/

"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
"""

# Backtracking
# Intially, we have N options, then N-1 then N-2 so N * (N-1) * (N-2) .. -> N!
# Time: O(N*N!) -> O(N!) .. also nPn == n!
# Space: O(N*N!) -> O(N!)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path_len, path, used):
            if n == path_len:
                res.append(path[:])

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:  # it can be used[i - 1] too
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path_len + 1, path, used)
                used[i] = False
                path.pop()

        res = []
        n = len(nums)
        nums.sort()
        backtrack(0, [], [False] * n)
        return res


# Smarter way to handle duplicates and without sorting
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path_len, path, counter):
            if n == path_len:
                res.append(path[:])

            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    path.append(num)
                    backtrack(path_len + 1, path, counter)
                    counter[num] += 1
                    path.pop()

        res = []
        n = len(nums)
        backtrack(0, [], Counter(nums))
        return res


# https://leetcode.com/problems/permutations-ii/discuss/18602/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others-%3A-)