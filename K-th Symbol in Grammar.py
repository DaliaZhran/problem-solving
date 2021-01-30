# https://leetcode.com/problems/k-th-symbol-in-grammar/

"""
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0
"""

# Brute Force
# Time : O(2^N) -> 1 + 2^2 + 2^3 + ... + 2^N
# Space : O(2^N)
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        curr = "0"
        for i in range(1, N + 1):
            next_row = ""
            for ch in curr:
                if ch == "0":
                    next_row += "01"
                else:
                    next_row += "10"
            curr = next_row

        return curr[K - 1]


# Recursion -> like a binary tree -> if K is even, flip parent val
# Time : O(N)
# Space : O(N)
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        if K % 2 == 0:
            return self.kthGrammar(N - 1, K // 2) ^ 1
        else:
            return self.kthGrammar(N - 1, (K + 1) // 2)


# same idea as prev solution but iterative
# Time : O(K)
# Space : O(1)
class Solution:
    def kthGrammar(self, N, K):
        res = 0
        while K > 1:
            K = K + 1 if K % 2 else K / 2
            res ^= 1
        return res


# Recursion -> flip variant -> if k in 1st half, then it is the same as the same k in prev row.
# if k in second half, then it is the complement of equivalent in prev row.
# Time : O(N)
# Space : O(N) -> No tail recursion optimization in python
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        half = 2 ** (N - 2)
        if K <= half:
            return self.kthGrammar(N - 1, K)
        else:
            return self.kthGrammar(N - 1, K - half) ^ 1


# the number of times we will flip the final answer is just the number of 1s in the binary representation of K-1.