# https://leetcode.com/problems/last-stone-weight/

"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
"""

from heapq import heappop, heappush


# Using Heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heappush(heap, -s)

        while len(heap) > 1:
            y = -heappop(heap)
            x = -heappop(heap)
            if y > x:
                heappush(heap, -(y - x))

        return 0 if not heap else -heappop(heap)
