# https://leetcode.com/problems/valid-perfect-square/


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, h = 0, num // 2
        while l <= h:
            mid = l + (h - l) // 2
            square = mid * mid
            if square == num:
                return True
            elif square > num:
                h = mid - 1
            else:
                l = mid + 1

        return False


# check newton's method