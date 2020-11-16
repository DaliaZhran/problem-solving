# https://leetcode.com/problems/powx-n/

"""
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
"""

# iterative brute force -> time limit exceed
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        for i in range(n):
            res = res * x

        return res


# * Recusrive Fast Power Algorithm
# Depneding on the fact that multiplying numbers with same base, we add powers. we can have x^(n/2), then multiply it by itself and get x ^ n. doo this recursively.
# time -> O(log2 n)
# space -> O(log2 n) .. stack calls
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fastPow(x: float, n: int) -> float:
            if n == 0:
                return 1.0
            half = fastPow(x, n // 2)
            powRes = half * half
            if n % 2 == 0:
                return powRes
            else:
                return x * powRes

        if n < 0:
            x = 1 / x
            n = -n

        return fastPow(x, n)


# better recursive implementation
class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)


# iterative fast power
# time -> O(log2 N)
# space -> O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n:
            if n & 1:
                res = res * x
            x *= x
            n = n >> 1
        return res