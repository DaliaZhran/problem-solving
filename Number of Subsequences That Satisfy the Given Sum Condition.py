# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

"""
Given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
"""

# Two Pointers
# Time: O(nlogn)
# Space: O(1)
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        nums.sort()
        count = 0
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                count += pow(2, r - l, mod)
                l += 1

        return count % mod


# number of subsequences of n length array -> 2^n = nC0 + nC1 + nC2 + ... + nCn

"""
Hope you got answer to your question by now. If not, here's my explanation.

Based on the constraints, given input array length lies anywhere between 1 & 10^5 (given 1 <= nums.length <= 10^5). So you're required to calculate 2 to the power 10^5 in this given scenario (left = 0, right = 10^5 - 1) which doesn't fit in the Integer number range and leads to overflow in certain programming languages thereby resulting in incorrect output.
Therefore doing a mod 10**9+7 overcomes this problem.

Why only 1e9 + 7 is being used? - 1e9 + 7 is the biggest prime number sufficient to return the right output after doing mod, in case of an overflow.

Follow the below links for better insights, if required.

https://www.geeks-for-geeks.org/modulo-1097-1000000007/
https://www.quora.com/What-exactly-is-print-it-modulo-10-9-+-7-in-competitive-programming-web-sites
"""
