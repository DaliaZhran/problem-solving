# https://leetcode.com/problems/grumpy-bookstore-owner/

"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
"""


# Sliding Window
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        if len(customers) <= X:
            return sum(customers)

        start = 0
        num_of_customers = 0  # number of customers when the owner is not grumpy (grumpy[i] = 0)
        max_missed_in_window_X = 0  # max number of missed customers when the owner is grumpy in window of size X
        curr_missed_in_window_X = 0

        for i in range(len(customers)):
            num_of_customers += customers[i] - customers[i] * grumpy[i]
            curr_missed_in_window_X += customers[i] * grumpy[i]

            if i >= X:
                curr_missed_in_window_X -= customers[start] * grumpy[start]
                start += 1

            max_missed_in_window_X = max(max_missed_in_window_X, curr_missed_in_window_X)

        return num_of_customers + max_missed_in_window_X
