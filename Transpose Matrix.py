# https://leetcode.com/problems/transpose-matrix/


# Time : O(rows*cols)
# Space : O(rows*cols)
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        cols = len(A[0])
        B = [[0] * rows for _ in range(cols)]
        for i in range(cols):
            for j in range(rows):
                B[i][j] = A[j][i]

        return B