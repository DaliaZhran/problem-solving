# https://leetcode.com/problems/house-robber-ii/

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
'''

# Bottom Up DP 
# Time: O(n), Where n is size of nums
# Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0: return 0
        if n < 3: return max(nums)
        
        return max(self.tryRob(nums[1:]), self.tryRob(nums[:-1]))
        
        
    def tryRob(self, nums):
        n = len(nums)
        p0 = 0
        p1 = nums[0]
        for i in range(2, n + 1):
            p0, p1 = p1, max(p1, nums[i - 1] + p0)
        
        return p1