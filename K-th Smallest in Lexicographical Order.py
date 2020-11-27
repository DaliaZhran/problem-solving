# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

"""
Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.

Note: 1 ≤ k ≤ n ≤ 109.
"""


# Good sol
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/92242/ConciseEasy-to-understand-Java-5ms-solution-with-Explaination


class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        min_heap = []
        for i in range(1, n + 1):
            min_heap.append(str(i))

        heapify(min_heap)
        for _ in range(1, k + 1):
            val = heappop(min_heap)
        return int(val)