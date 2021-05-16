# https://leetcode.com/problems/valid-number/

"""
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
"""

# time: O(N)
# space: O(N) for slicing string
class Solution:
    def isNumber(self, s: str) -> bool:
        s_length = len(s)
        if s_length == 1:
            return s.isnumeric()
        if s[0] in "eE":
            return False

        # check if decimal
        dot = 0
        num = 0
        for i in range(s_length):
            if i != 0 and s[i] in "+-" or s[i] not in "eE" and s[i].isalpha():
                return False
            elif s[i] in "eE":
                if i == 0 or num == 0:
                    return False
                return self.checkIfInt(s[i + 1 :])
            elif s[i] == ".":
                if dot == 1:
                    return False
                dot = 1
            elif s[i].isdigit():
                num = 1
        return num

    def checkIfInt(self, s):
        if len(s) < 2:
            return s.isnumeric()
        if s.isnumeric() or s[0] in "+-" and s[1:].isnumeric():
            return True
        else:
            return False


# time: O(N)
# space: O(1)
class Solution:
    def isNumber(self, s: str) -> bool:
        s_length = len(s)
        if s_length == 1:
            return s.isnumeric()
        if s[0] in "eE":
            return False

        # check if decimal
        dot = num = exp = 0
        for i in range(s_length):
            if s[i] in "+-":
                if i > 0 and s[i - 1] not in "eE":
                    return False
            elif s[i] in "eE":
                if exp == 1 or num == 0:
                    return False
                exp = 1
                num = 0
            elif s[i] == ".":
                if dot == 1 or exp == 1:
                    return False
                dot = 1
            elif s[i].isdigit():
                num = 1
            else:
                return False
        return num


# check groups (DA) solutions
