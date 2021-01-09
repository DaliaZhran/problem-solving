# https://leetcode.com/problems/climbing-stairs/


# Brute Force - Recursive
# Time : O(2^n)
# Space: O(n)
class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        def climbStairsRecursive(i):
            if i > n:
                return 0
            if i == n:
                return 1
            return climbStairsRecursive(i + 1) + climbStairsRecursive(i + 2)

        return climbStairsRecursive(0)


# Recursive with Memoization
# Time : O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climbStairsRecursive(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]

            ans = climbStairsRecursive(i + 1) + climbStairsRecursive(i + 2)
            memo[i] = ans
            return ans

        return climbStairsRecursive(0)


# Approach 4: DP
# Time : O(n)
# Space: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Approach 4: Fibonacci Number
# Time : O(n)
# Space: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 2

        curr = 0
        prev1 = 2
        prev2 = 1

        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return curr
