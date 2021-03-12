# https://leetcode.com/problems/interleaving-string/

# Approach 1: Brute Force
# Time: O(2^(n+m))
# Space: O(n + m)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def isInterleaveRecursive(i1, i2, i3):
            if i1 == n1 and i2 == n2 and i3 == n3:
                return True

            if i3 == n3:
                return False

            op1, op2 = False, False
            if i1 < n1 and s1[i1] == s3[i3]:
                op1 = isInterleaveRecursive(i1 + 1, i2, i3 + 1)

            if i2 < n2 and s2[i2] == s3[i3]:
                op2 = isInterleaveRecursive(i1, i2 + 1, i3 + 1)

            return op1 or op2

        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        return isInterleaveRecursive(0, 0, 0)


# Approach 2: Recursion with memoization
# Time: O(m * n)
# Space: O(m * n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def isInterleaveRecursive(i1, i2, i3):
            if i1 == n1 and i2 == n2 and i3 == n3:
                return True

            if i3 == n3:
                return False

            key = str(i1) + "-" + str(i2) + "-" + str(i3)
            if key in dp:
                return dp[key]

            op1, op2 = False, False
            if i1 < n1 and s1[i1] == s3[i3]:
                op1 = isInterleaveRecursive(i1 + 1, i2, i3 + 1)

            if i2 < n2 and s2[i2] == s3[i3]:
                op2 = isInterleaveRecursive(i1, i2 + 1, i3 + 1)

            dp[key] = op1 or op2
            return dp[key]

        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        dp = {}
        return isInterleaveRecursive(0, 0, 0)


# TO DO: Bottom up DP
