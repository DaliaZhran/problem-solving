# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

"""
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
"""


# time: O(4n)
# space: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []  # increased number of '('
        indices_to_remove = set()  # increased number of ')'
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            if ch == ")":
                if not stack:
                    indices_to_remove.add(i)
                else:
                    stack.pop()
        indices_to_remove = indices_to_remove.union(set(stack))
        res = []
        for i, ch in enumerate(s):
            if i not in indices_to_remove:
                res.append(ch)
        return "".join(res)


# time: O(2n)
# space: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def delete_invalid_closing(string, open_symbol, close_symbol):
            sb = []
            balance = 0
            for c in string:
                if c == open_symbol:
                    balance += 1
                if c == close_symbol:
                    if balance == 0:
                        continue
                    balance -= 1
                sb.append(c)
            return "".join(sb)

        # Note that s[::-1] gets the reverse of s.
        s = delete_invalid_closing(s, "(", ")")
        s = delete_invalid_closing(s[::-1], ")", "(")
        return s[::-1]


# time: O(2n)
# space: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_par = balance = 0
        first_pass = []
        # remove increased number of ')'
        for ch in s:
            if ch == "(":
                open_par += 1
                balance += 1
            elif ch == ")":
                if balance == 0:
                    continue
                balance -= 1
            first_pass.append(ch)
        # balance is now the increased number of '(' in the string that we need to remove
        open_to_keep = open_par - balance
        result = []
        for ch in first_pass:
            if ch == "(":
                if open_to_keep == 0:
                    continue
                open_to_keep -= 1
            result.append(ch)
        return "".join(result)


# one pass
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/663204/Super-simple-Python-solution-with-explanation.-Faster-than-100-Memory-Usage-less-than-100
