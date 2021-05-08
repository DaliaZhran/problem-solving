# https://leetcode.com/problems/kth-largest-element-in-an-array/

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
"""
from heapq import *
from typing import List

# approach 1: sort and then return k from end

# approach 2: heap
# idea is to keep only the k large elements in a heap and the smallest one would be our target
# Time -> O(N * log k)
# Space -> O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heappush(heap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heappop(heap)
                heappush(heap, nums[i])

        return heap[0]


# approach 3: heap

"""
Making a heap from n elements actually takes linear time using heapify algorithm.

Python implementation of heapify uses a Bottom-Up (see e.g. Data Structures and Algorithms by Goodrich) heap construction algorithm that is more efficient and makes construction of a heap with N elements O(N) and not O(N log N) because insertion is not O(log N) as one might think.

we can trade off space with time and create the heap with all elements from beggining with O(N) time and space
"""
