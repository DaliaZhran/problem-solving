# https://leetcode.com/problems/subarrays-with-k-different-integers/

"""
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
"""
from collections import defaultdict
from typing import List


# Time: O(N)
# Space: O(1)
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.subarrayswithAtMostKDistinct(A, K) - self.subarrayswithAtMostKDistinct(A, K - 1)

    def subarrayswithAtMostKDistinct(self, A: List[int], k: int) -> int:
        start = 0
        count = 0
        char_map = defaultdict(int)
        for end in range(len(A)):
            char_map[A[end]] += 1

            while len(char_map) > k:
                char_map[A[start]] -= 1
                if char_map[A[start]] == 0:
                    del char_map[A[start]]
                start += 1

            count += end - start

        return count
