# https://leetcode.com/problems/fibonacci-number/

# Approach 1: Recursion
# Time : O(2^n)
# Space: O(n)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


# Approach 2: Bottom-Up Approach using Memoization
# Time : O(n)
# Space: O(n)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        memo = {0: 0, 1: 1}
        for i in range(2, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]


# Approach 3: Top-Down Approach using Memoization
# Time : O(n)
# Space: O(n)
class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def memoize(k):
            if k in memo:
                return memo[k]
            memo[k] = memoize(k - 1) + memoize(k - 2)
            return memo[k]

        if n <= 1:
            return n

        return memoize(n)


# Approach 4: Iterative Top-Down Approach
# Time : O(n)
# Space: O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1

        curr = 0
        prev1 = 1
        prev2 = 1

        for i in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr

        return curr
