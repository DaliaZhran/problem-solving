# https://leetcode.com/problems/coin-change-2/

"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""


# Brute Force Recursive -> [TLE]
# Time: O(2^(C+T​)), where ‘C’ represents total coin denominations and ‘T’ is the total amount that we want to make change.
# Space: O(C+T)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def explore(total, curr_idx):
            if total == 0:
                return 1

            if total < 0 or curr_idx >= n:
                return 0

            res1 = 0
            if coins[curr_idx] <= total:
                res1 = explore(total - coins[curr_idx], curr_idx)

            res2 = explore(total, curr_idx + 1)

            return res1 + res2

        n = len(coins)
        return explore(amount, 0)


# Top-down Dynamic Programming with Memoization
# Time: O(C∗T)
# Space: O(C∗T)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def explore(total, curr_idx):
            if total == 0:
                return 1

            if total < 0 or curr_idx >= n:
                return 0

            if dp[curr_idx][total] != -1:
                return dp[curr_idx][total]

            res1 = 0
            if coins[curr_idx] <= total:
                res1 = explore(total - coins[curr_idx], curr_idx)

            res2 = explore(total, curr_idx + 1)

            dp[curr_idx][total] = res1 + res2
            return dp[curr_idx][total]

        n = len(coins)
        dp = [[0] + [-1] * amount for _ in range(n)]
        return explore(amount, 0)


# Bottom-up Dynamic Programming
# Time: O(C∗T)
# Space: O(C∗T)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        if amount == 0:
            return 1
        if n == 0:
            return 0

        dp = [[1] + [0] * amount for _ in range(n)]

        for i in range(n):
            for amt in range(1, amount + 1):
                if i > 0:
                    dp[i][amt] = dp[i - 1][amt]
                if coins[i] <= amt:
                    dp[i][amt] += dp[i][amt - coins[i]]

        return dp[-1][-1]


# Fine Tuning - Bottom-up Dynamic Programming
# Time: O(C∗T) where ‘C’ represents total coin denominations and ‘T’ is the total amount that we want to make change.
# Space: O(T)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt - coin]

        return dp[-1]
