# https://leetcode.com/problems/valid-parentheses/

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""

# * Stack
# Time -> O(N)
# Space -> O(N)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in ")}]":
                if stack and stack[-1] == mapping[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return stack == []