# https://leetcode.com/problems/count-of-smaller-numbers-after-self/

"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
"""

# Brute Force Solution
# Time: O(N^2)
# Space: O(N)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    counts[i] += 1
        return counts


# Merge Sort
# Time: O(N log N)
# Space: O(N)
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(indexes):
            mid = len(indexes) // 2
            if mid:
                left = sort(indexes[:mid])
                right = sort(indexes[mid:])

                for i in range(len(indexes) - 1, -1, -1):
                    if not right or left and nums[left[-1]] > nums[right[-1]]:
                        # the whole right subarray are smaller than the last elem in left subarray
                        result[left[-1]] += len(right)
                        # the last elem in left is the largest number right now
                        indexes[i] = left.pop()
                    else:
                        indexes[i] = right.pop()  # no inversions so we just sort
            return indexes

        n = len(nums)
        result = [0] * n
        sort(list(range(n)))
        return result


# Enumerate idea -> https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution
# Good Explanation -> https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/445769/merge-sort-CLEAR-simple-EXPLANATION-with-EXAMPLES-O(n-lg-n)