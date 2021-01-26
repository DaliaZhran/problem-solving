# https://leetcode.com/problems/unique-binary-search-trees/

"""
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
"""

# Recursive Catalan's Number Calculation
# Time : exponential -> O(3^N)
# Space : exponential
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1

        Result = 0
        for i in range(n):
            LeftTrees = self.numTrees(i)
            RightTrees = self.numTrees(n - i - 1)
            Result += LeftTrees * RightTrees
        return Result


# Recursive DP Catalan's Number Calculation
# Time : O(N^2)
# Space : O(2*N)
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)

        def numTreesRecursive(n):
            if G[n]:
                return G[n]
            if n == 0 or n == 1:
                return 1

            # sum = 0
            # for i in range(1, n + 1):
            #     sum += numTreesRecursive(i - 1) * numTreesRecursive(n - i)
            # G[n] = sum

            for i in range(1, n + 1):
                G[n] += numTreesRecursive(i - 1) * numTreesRecursive(n - i)

            return G[n]

        return numTreesRecursive(n)


# Iterative DP Catalan's Number Calculation
# Time : O(N^2)
# Space : O(N)
class Solution:
    def numTrees(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0] = G[1] = 1

        for i in range(2, n + 1):  # G(2) = F(1,2) + F(2,2) = G(1) * G(0)
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]

        return G[n]


# Binomial Coefficients
# Time : O(n)
# Space : O(1)
class Solution:
    def numTrees(self, n: int) -> int:
        C = 1
        for i in range(1, n):
            C = C * 2 * (2 * i + 1) // (i + 2)
        return C