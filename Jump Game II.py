# https://leetcode.com/problems/jump-game-ii/

'''
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

# Brute Force -> TLE
# Time: O(k^n), Where, k is max element of nums and n is size of nums
# Space: O(n) for stack
class Solution:
    def jump(self, nums: List[int]) -> int:
        def tryJump(index):
            if index == n - 1:
                return 0
            if nums[index] == 0:
                return float('inf')
            
            min_jumps = float('inf')
            start = index + 1
            end = index + nums[index]
            while start < n and start <= end:
                count = tryJump(start)
                start += 1
                if count != float('inf'):
                    min_jumps = min(min_jumps, count + 1)
            
            return min_jumps
        
        n = len(nums)
        return tryJump(0)
        


# Memoization -> TLE
# Time : O(k * n), Where k is max element of nums and n is size of nums.
# Space: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        def tryJump(index):
            if index == n - 1:
                return 0
            if nums[index] == 0:
                return float('inf')
            if dp[index] != 0:
                return dp[index]
            
            min_jumps = float('inf')
            start = index + 1
            end = index + nums[index]
            while start < n and start <= end:
                count = tryJump(start)
                start += 1
                if count != float('inf'):
                    min_jumps = min(min_jumps, count + 1)
            
            dp[index] = min_jumps
            return min_jumps
        
        n = len(nums)
        dp = [0] * n
        return tryJump(0)
        
        

# Top Down DP -> TLE
# Time : O(k * n), Where k is max element of nums and n is size of nums.
# Space: O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        
        for curr in range(n - 1):
            step = curr + 1
            end = curr + nums[curr]
            while step < n and step <= end:
                dp[step] = min(dp[step], dp[curr] + 1)
                step += 1
            
        return dp[-1]



# Approach 4: Greedy
# Time: O(n), Where ‘n’ is the size of the input array
# Space: O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        count = curr_end = curr_farthest = 0
        
        for i in range(n - 1):
            curr_farthest = max(curr_farthest, i + nums[i])
            if i == curr_end:
                count += 1
                curr_end = curr_farthest
            
        return count
    