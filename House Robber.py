# https://leetcode.com/problems/house-robber/

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
'''

# Brute Force -> TLE
# Time: O(2 ^ n), Where n is size of nums
# Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def tryRob(idx):
            if idx >= n:
                return 0
            
            max_money = max(tryRob(idx + 1), nums[idx] + tryRob(idx + 2))
            return max_money
        
        n = len(nums)
        return tryRob(0)
    


# Memoization -> TLE
# Time: O(n), Where n is size of nums
# Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        def tryRob(idx):
            if idx >= n:
                return 0
            
            if dp[idx] == 0:
                dp[idx] = max(tryRob(idx + 1), nums[idx] + tryRob(idx + 2))
            
            return dp[idx]
        
        n = len(nums)
        dp = [0] * n
        return tryRob(0)
    



# Bottom Up DP 
# Time: O(n), Where n is size of nums
# Space: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0: return 0
        if n < 3: return max(nums)
        
        dp = [0] * (n)
        dp[0] = 0
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i-2])
        
        # for i in range(1, n + 1):
        #     dp[i + 1] = max(dp[i], nums[i] + dp[i - 1])
        
        return dp[-1]



# Bottom Up DP 
# Time: O(n), Where n is size of nums
# Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0: return 0
        if n < 3: return max(nums)
        
        p0 = 0
        p1 = nums[0]
        for i in range(2, n + 1):
            p0, p1 = p1, max(p1, nums[i - 1] + p0)
        
        return p1