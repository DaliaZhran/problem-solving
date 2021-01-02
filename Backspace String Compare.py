# https://leetcode.com/problems/backspace-string-compare/

"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
"""

# * Approach 1: Stack
# Time: O(N)
# Space: O(N)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.buildString(S) == self.buildString(T)

    def buildString(self, string: str):
        stack = []
        for ch in string:
            if ch != "#":
                stack.append(ch)
            elif stack:
                stack.pop()
        return "".join(stack)


# * Approach 2: Two Pointers
# Time: O(N)
# Space: O(1)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_ptr, t_ptr = len(S) - 1, len(T) - 1
        s_cnt, t_cnt = 0, 0  # count of letters to skip in S and T, respectively

        while s_ptr >= 0 or t_ptr >= 0:
            # skip all # in S or letters to skip
            while s_ptr >= 0 and (S[s_ptr] == "#" or s_cnt):
                s_cnt += 1 if S[s_ptr] == "#" else -1
                s_ptr -= 1

            # skip all # in T or letters to skip
            while t_ptr >= 0 and (T[t_ptr] == "#" or t_cnt):
                t_cnt += 1 if T[t_ptr] == "#" else -1
                t_ptr -= 1

            # check if the current indexes are equal
            if not (s_ptr >= 0 and t_ptr >= 0 and S[s_ptr] == T[t_ptr]):
                # if the pointer are -1, it means we traversed all the chars in both strings
                return s_ptr == t_ptr == -1

            s_ptr -= 1
            t_ptr -= 1

        return True
