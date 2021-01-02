# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

"""
There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
"""


# idea is to start with the min ratio and then move to larger ones while minimizing the sum of qualities
# Time Complexity: O(NlogN), where N is the number of workers.
# Space Complexity: O(N).
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        workers = [(float(w) / q, q) for w, q in zip(wage, quality)]
        max_heap = []
        min_wages = float("inf")
        sum_qualities = 0

        for ratio, q in sorted(workers):
            heappush(max_heap, -q)
            sum_qualities += q
            if len(max_heap) > K:
                sum_qualities += heappop(max_heap)  # here we + because push negative qualities to the heap
            if len(max_heap) == K:
                min_wages = min(min_wages, sum_qualities * ratio)

        return min_wages