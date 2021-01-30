# https://leetcode.com/problems/generate-parentheses/

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

# Approach 1: Brute Force


# Approach 2: Backtracking
# Time: O(2^2n)
# Space: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, left=0, right=0):
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return

            if left < n:
                curr.append("(")
                backtrack(curr, left + 1, right)
                curr.pop()

            if right < left:
                curr.append(")")
                backtrack(curr, left, right + 1)
                curr.pop()

        res = []
        backtrack([])
        return res