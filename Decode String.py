# https://leetcode.com/problems/decode-string/

"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"
"""

# Using a Stack
# Time : O(N^2) where N is len(s)
# Space : O(N)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        for ch in s:
            if ch != "]":
                # string can have numbers not only digits
                # if the stack peak and curr char is numeric then we should concatenate them to form a num
                if stack and stack[-1].isnumeric() and ch.isnumeric():
                    stack.append(stack.pop() + ch)
                else:
                    stack.append(ch)
            else:
                word = deque()
                # encode the last bracket
                while stack[-1] != "[":
                    word.appendleft(stack.pop())
                # pop the '[' char
                stack.pop()
                # get the number of repeatitions
                multiplier = stack.pop()
                # append the decoded string to the stack to continue encoding it if it is a nested encoded string
                stack.append("".join(word) * int(multiplier))

        # the stack now has all the decoded strings
        return "".join(stack)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isnumeric():
                num += ch
            elif ch == "[":
                stack.append(["", int(num)])
                num = ""
            elif ch == "]":
                string, k = stack.pop()
                stack[-1][0] += string * k
            else:
                stack[-1][0] += ch

        return stack[0][0]


# https://leetcode.com/submissions/detail/276052975/