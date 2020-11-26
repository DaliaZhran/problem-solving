class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j, start, end = 0, 0, 0, 1
        result = []
        while i < len(A) and j < len(B):
            AB = A[i][start] <= B[j][start] and A[i][end] >= B[j][start]
            BA = B[j][start] <= A[i][start] and B[j][end] >= A[i][start]

            if AB or BA:
                result.append([max(A[i][start], B[j][start]),
                               min(A[i][end], B[j][end])])

            if A[i][end] < B[j][end]:
                i += 1
            else:
                j += 1
        return result
