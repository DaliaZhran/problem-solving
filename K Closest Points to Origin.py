# https://leetcode.com/problems/k-closest-points-to-origin/

"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
"""

from heapq import heappop, heappush


# * Approach 1: Sort
# Time -> O(n log n) where n is the number of all points
# Space -> O(n)
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
        return points[:K]


# * Approach 2: Heap
# Time -> O(n log K) where n is the number of all points and log(K) is the cost of adding and removing items from the heap
# Space -> O(K) -> space used by heap
class Solution(object):
    def calculateDistance(self, point):
        return point[0] * point[0] + point[1] * point[1]  # ignore the sqrt since we are just comparing points to each other

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        min_heap = []
        for i in range(K):
            heappush(min_heap, (-1 * self.calculateDistance(points[i]), i))

        for i in range(K, len(points)):
            if -1 * self.calculateDistance(points[i]) > min_heap[0][0]:
                heappop(min_heap)
                heappush(min_heap, (-1 * self.calculateDistance(points[i]), i))

        return [points[x[1]] for x in min_heap]