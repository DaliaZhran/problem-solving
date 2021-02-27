# https://leetcode.com/problems/contains-duplicate-iii/


# Linear Search
# Time: O(n min(n, k))
# Space: O(1)
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):
                if abs(nums[i] - nums[j]) <= t:
                    return True
        return False


# Using libraries -> SortedList and bisect
# Time: O(n log k)
# Space: O(k)
from sortedcontainers import SortedList
from bisect import bisect_left, bisect_right


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = SortedList()
        for i, num in enumerate(nums):
            if i > k:
                window.remove(nums[i - k - 1])
            pos1 = bisect_left(window, num - t)
            pos2 = bisect_right(window, num + t)
            if pos1 != pos2:
                return True
            window.add(num)

        return False


# check bucket sort algorithm to solve this