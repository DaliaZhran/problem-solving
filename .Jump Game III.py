# https://leetcode.com/problems/jump-game-iii/

'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array.
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
'''

from collections import deque

# Use BFS
# * Time complexity: O(N)
# * Space complexity: O(N)
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)
        q = deque([start])

        while q:
            node = q.popleft()
            if arr[node] == 0:
                return True
            if arr[node] < 0:
                continue
            for child in [node + arr[node], node - arr[node]]:
                if 0 <= child < n:
                    q.append(child)

            arr[node] = -arr[node]  # to recognize already visited nodes


# DFS
# * Time complexity: O(N)
# * Space complexity: O(N)
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        n = len(arr)

        def canReachDFS(node):
            if 0 <= node < n and arr[node] == 0:
                return True
            if 0 <= node < n and arr[node] > 0:
                arr[node] = -arr[node]
                return canReachDFS(node + arr[node]) or canReachDFS(node - arr[node])
            return False

        return canReachDFS(start)
