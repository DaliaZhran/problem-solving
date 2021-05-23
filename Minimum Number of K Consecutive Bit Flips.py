# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/
"""
In an array nums containing only 0s and 1s, a k-bit flip consists of choosing a (contiguous) subarray of length k and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

 
Example 1:
Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].

Example 2:
Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].

Example 3:
Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation:
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]
"""
from typing import List


# Brute Force -> TLE
# Time: O(N * K) where N is len(A)
# Space: O(K)
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        start = count = 0
        while start + K - 1 < n:
            if A[start] == 1:
                start += 1
                continue
            count += 1
            for i in range(start, start + K):
                A[i] ^= 1

        return count
