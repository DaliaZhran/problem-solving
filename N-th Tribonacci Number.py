# https://leetcode.com/problems/n-th-tribonacci-number/
"""
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""

# sol 1-> normal for loop
# time -> O(n)
# space -> O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 2:
            return 1

        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z


# prepare in the solution all numbers first to avoid calculating each time since n < 38
# time -> O(1)
# space -> O(1) since array is always of size 38
class Tribonacci(object):
    def __init__(self):
        def tribonacciDFS(k):
            if k == 0:
                return 0
            if self.nums[k]:
                return self.nums[k]

            self.nums[k] = tribonacciDFS(k - 1) + tribonacciDFS(k - 2) + tribonacciDFS(k - 3)

            return self.nums[k]

        n = 38
        self.nums = [0] * n
        self.nums[0], self.nums[1], self.nums[2] = 0, 1, 1
        tribonacciDFS(n - 1)


class Solution(object):
    sol = Tribonacci()

    def tribonacci(self, n: int) -> int:
        return self.sol.nums[n]


# prepare in the solution all numbers first to avoid calculating each time since n < 38 but this time using iterations not recursion (DP)
# time -> O(1)
# space -> O(1) since array is always of size 38
class Tribonacci(object):
    def __init__(self):
        n = 38
        self.nums = [0] * n
        self.nums[0], self.nums[1], self.nums[2] = 0, 1, 1

        for i in range(3, n):
            self.nums[i] = self.nums[i - 1] + self.nums[i - 2] + self.nums[i - 3]


class Solution(object):
    sol = Tribonacci()

    def tribonacci(self, n: int) -> int:
        return self.sol.nums[n]
