# https://leetcode.com/problems/unique-paths-ii/


# DP
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = 1 if obstacleGrid[i][0] == 0 and dp[i - 1][0] == 1 else 0

        for j in range(1, n):
            dp[0][j] = 1 if obstacleGrid[0][j] == 0 and dp[0][j - 1] == 1 else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

        return dp[-1][-1]
