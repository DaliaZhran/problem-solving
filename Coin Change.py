# https://leetcode.com/problems/coin-change/

"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
"""

# Brute Force -> Recursive [Time Limit Exceeded]
# Time -> O(amount^n) -> n is len(coins)
# Space -> O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def count_coins(coin_index, remaining):
            if remaining == 0:
                return 0

            if coin_index < n and remaining > 0:
                min_cost = float("inf")
                max_count = remaining // coins[coin_index]
                for x in range(max_count + 1):
                    count = count_coins(coin_index + 1, remaining - x * coins[coin_index])
                    if count != -1:
                        min_cost = min(min_cost, count + x)
                return min_cost if min_cost != float("inf") else -1

            return -1

        n = len(coins)
        return count_coins(0, amount)


# Brute Force -> Recursive [Time Limit Exceeded]
# Better for the optimization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def count_coins(remaining):
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0
            # if dp[remaining] != 0:
            #     return dp[remaining]

            min_cost = float("inf")
            for coin in coins:
                res = count_coins(remaining - coin)
                if res >= 0:
                    min_cost = min(res + 1, min_cost)

            # dp[remaining] = min_cost if min_cost != float('inf') else -1
            return min_cost if min_cost != float("inf") else -1
            # return dp[remaining]

        if amount < 1:
            return 0
        # dp = [0] * (amount + 1)
        return count_coins(amount, 0)


# Top Down DP (Memoization)
# Time: O(amount * n)
# Space: O(amount)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def count_coins(remaining):
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0
            if dp[remaining] != 0:
                return dp[remaining]

            min_cost = float("inf")
            for coin in coins:
                res = count_coins(remaining - coin)
                if res >= 0:
                    min_cost = min(res + 1, min_cost)

            dp[remaining] = min_cost if min_cost != float("inf") else -1
            return dp[remaining]

        if amount < 1:
            return 0
        dp = [0] * (amount + 1)
        return count_coins(amount, 0)
