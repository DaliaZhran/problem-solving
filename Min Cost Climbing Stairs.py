# https://leetcode.com/problems/min-cost-climbing-stairs/


"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
"""

# Goood Approach -> https://leetcode.com/problems/min-cost-climbing-stairs/discuss/476388/4-ways-or-Step-by-step-from-Recursion-greater-top-down-DP-greater-bottom-up-DP-greater-fine-tuning

# https://leetcode.com/problems/min-cost-climbing-stairs/discuss/773865/A-Beginner's-Guide-on-DP-validation-and-How-to-come-up-with-a-Recursive-solution-Python-3


# Step 1 - Identify a recurrence relation between subproblems. In this problem,
# Recurrence Relation:
# mincost(i) = cost[i]+min(mincost(i-1), mincost(i-2))
# Base cases:
# mincost(0) = cost[0]
# mincost(1) = cost[1]


# Step 2 - Covert the recurrence relation to recursion
# Time: O(2^n) -> [Time Limit Exceeded]
# Space: O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(i):
            if i < 2:
                return cost[i]
            return cost[i] + min(helper(i-1), helper(i-2))
        
        n = len(cost)
        return min(helper(n - 1), helper(n - 2)) # this is the trick here


# Step 3 - Optimization 1 - Top Down DP - Add memoization to recursion - From exponential to linear.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minCost(n):
            if n < 0:
                return 0
            elif n < 2:
                dp[n] = cost[n]
            elif dp[n] != 0:
                return dp[n]

            dp[n] = cost[n] + min(minCost(n - 1), minCost(n - 2))
            return dp[n]

        n = len(cost)
        dp = [0] * n
        return min(minCost(n - 1), minCost(n - 2))


# Step 4 - Optimization 2 - Bottom Up DP - Convert recursion to iteration - Getting rid of recursive stack
# General Bottom-Up Approach
# Time: O(N)
# Space: O(N)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:]
        for i in range(2, len(cost)):
            dp[i] += min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])
        


# Step 5 - Optimization 3 - Fine Tuning - Reduce O(n) space to O(1).
# Time: O(N)
# Space: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev0 = cost[0]
        prev1 = cost[1]
        for i in range(2, len(cost)):
            prev0, prev1 = prev1, cost[i] + min(prev0, prev1)
            
        return min(prev0, prev1)
        


# For the brute force recursive solution, it is better to use direct recursion instead of side-effect to make it easy to use memoization then