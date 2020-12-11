# https://leetcode.com/problems/maximum-performance-of-a-team/

"""
There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. 

 

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
"""
from heapq import heappop, heappush


class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []
        res = 0
        sp_sum = 0
        for eff, sp in sorted(zip(efficiency, speed), reverse=1):
            heappush(min_heap, sp)
            sp_sum += sp
            if len(min_heap) > k:
                sp_sum -= heappop(min_heap)
            res = max(res, sp_sum * eff)
        return res % (10 ** 9 + 7)


# without the k constraint
class Solution:
    def maxPerformance_simple(self, n, speed, efficiency):

        people = sorted(zip(speed, efficiency), key=lambda x: -x[1])

        result, sum_speed = 0, 0

        for s, e in people:
            sum_speed += s
            result = max(result, sum_speed * e)

        return result  # % 1000000007


# https://leetcode.com/problems/maximum-performance-of-a-team/discuss/741822/Met-this-problem-in-my-interview!!!-(Python3-greedy-with-heap)