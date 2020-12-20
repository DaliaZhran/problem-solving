# https://leetcode.com/problems/maximize-distance-to-closest-person/

"""
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.
"""

# * Approach 1: Two Pointers - One Pass
# Time : O(n)
# Space : O(1)
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_dist = 0
        prev = -1

        for i, seat in enumerate(seats):
            if seat == 1:
                if prev == -1:
                    max_dist = max(max_dist, i)  # distance between fist element and first 1
                else:
                    max_dist = max(max_dist, (i - prev) / 2)  # distance between any 2 ones

                prev = i

        # if last element is zero, we need to check the distance between it and the prev one too
        # if last element is 1, then i - prev = 0
        return max(max_dist, i - prev)  # i = len(seats)


# * Approach 2: max consecutive zeros and divide by 2
# Time : O(n)
# Space : O(n) due to the seats[::-1]
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        consequentZero, ans = 0, 0
        for s in seats:
            if s == 0:
                consequentZero += 1
                ans = max(ans, consequentZero)
            else:
                consequentZero = 0
        ans = (ans + 1) // 2
        return max(ans, seats.index(1), seats[::-1].index(1))  # check distance at the beginning and at the end of array
