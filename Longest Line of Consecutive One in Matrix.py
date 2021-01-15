# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        rows = len(M)
        cols = len(M[0])
        # [0,0,0,0] -> [horizontal, vertical, diagonal, anti-diagonal]
        dp = [[[0, 0, 0, 0] for _ in range(cols)] for __ in range(rows)]
        ones = 0
        for i in range(rows):
            for j in range(cols):
                if M[i][j] == 1:
                    dp[i][j][0] = 1 if j < 1 else dp[i][j - 1][0] + 1  # horizontal
                    dp[i][j][1] = 1 if i < 1 else dp[i - 1][j][1] + 1  # vertical
                    dp[i][j][2] = 1 if i < 1 or j < 1 else dp[i - 1][j - 1][2] + 1  # diagonal
                    dp[i][j][3] = 1 if i < 1 or j + 1 >= cols else dp[i - 1][j + 1][3] + 1  # anti-diagonal

                    ones = max(ones, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        return ones
