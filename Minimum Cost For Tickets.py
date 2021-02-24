# https://leetcode.com/problems/minimum-cost-for-tickets/

"""
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
"""

# Recursive
# Time: O(3^n) -> n is len(days)
# Space: O(n)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def helper(idx):
            if idx >= n:
                return 0

            cost_day = costs[0] + helper(idx + 1)

            i = idx
            while i < n and days[i] < days[idx] + 7:
                i += 1
            cost_week = costs[1] + helper(i)

            i = idx
            while i < n and days[i] < days[idx] + 30:
                i += 1
            cost_month = costs[2] + helper(i)

            return min(cost_day, cost_week, cost_month)

        n = len(days)
        return helper(0)


# Top Down Memoization
# Time: O(n)
# Space: O(n)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def helper(idx):
            if idx >= n:
                return 0

            if dp[idx]:
                return dp[idx]

            cost_day = costs[0] + helper(idx + 1)

            i = idx
            while i < n and days[i] < days[idx] + 7:
                i += 1
            cost_week = costs[1] + helper(i)

            i = idx
            while i < n and days[i] < days[idx] + 30:
                i += 1
            cost_month = costs[2] + helper(i)

            dp[idx] = min(cost_day, cost_week, cost_month)
            return dp[idx]

        n = len(days)
        dp = [0] * n
        return helper(0)


# Bottom Up DP
# Time: O(365)
# Space: O(365)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        days_set = set(days)
        dp = [0] * 366

        for i in range(1, 366):
            dp[i] = dp[i - 1]
            if i in days_set:
                dp[i] = min(costs[0] + dp[max(0, i - 1)], costs[1] + dp[max(0, i - 7)], costs[2] + dp[max(0, i - 30)])

        return dp[-1]


# Check Fine Tuning
# https://leetcode.com/problems/minimum-cost-for-tickets/discuss/226659/Two-DP-solutions-with-pictures