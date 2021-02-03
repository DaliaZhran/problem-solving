# https://leetcode.com/problems/strobogrammatic-number/

"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.
"""

# Time: O(N) -> N is len(num)
# Space: O(N)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated = []

        for c in reversed(num):
            if c in {"0", "1", "8"}:
                rotated.append(c)
            elif c == "6":
                rotated.append("9")
            elif c == "9":
                rotated.append("6")
            else:
                return False

        rotated = "".join(rotated)
        return rotated == num


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mp = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        rotated = []

        for c in reversed(num):
            if c in mp:
                rotated.append(mp[c])
            else:
                return False

        rotated = "".join(rotated)
        return rotated == num


# Time: O(N)
# Space: O(1)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mp = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}

        start, end = 0, len(num) - 1
        while start <= end:
            if num[start] not in mp or mp[num[start]] != num[end]:
                return False
            start += 1
            end -= 1

        return True