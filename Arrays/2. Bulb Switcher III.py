# https://leetcode.com/problems/bulb-switcher-iii/

"""
There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.
"""


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        all_blue_moments = rightmost = on = 0
        for bulb in light:
            on += 1
            rightmost = max(rightmost, bulb)
            if on == rightmost:
                all_blue_moments += 1
        return all_blue_moments


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        all_blue_moments = rightmost = 0
        for i, bulb in enumerate(light):
            rightmost = max(rightmost, bulb)
            if i + 1 == rightmost:
                all_blue_moments += 1
        return all_blue_moments