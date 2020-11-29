# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
"""


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        max_heap = []
        for i in range(min(len(nums1), k)):
            for j in range(len(nums2)):
                if len(max_heap) < k:
                    heappush(max_heap, (-nums1[i] - nums2[j], i, j))
                else:
                    if nums1[i] + nums2[j] < -max_heap[0][0]:
                        heappop(max_heap)
                        heappush(max_heap, (-nums1[i] - nums2[j], i, j))
                    else:
                        break

        pairs = []
        for s, i, j in max_heap:
            pairs.append([nums1[i], nums2[j]])

        return pairs


# check other solutions -> https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation