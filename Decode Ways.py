# https://leetcode.com/problems/decode-ways/

# DFS with memoization
# Time: O(N) since we decode each index once
# Space: O(N) since the memoization set would contain indecies up to len(s). same for recursion stack too
class Solution:
    def __init__(self):
        self.memo = {}

    def decode_with_memo(self, index: int, s: str) -> int:
        if index == len(s):
            return 1

        if s[index] == "0":
            return 0

        if index == len(s) - 1:
            return 1

        if index in self.memo:
            return self.memo[index]

        if s[index : index + 2] <= "26":
            ans = self.decode_with_memo(index + 1, s) + self.decode_with_memo(index + 2, s)
        else:
            ans = self.decode_with_memo(index + 1, s)

        self.memo[index] = ans
        return ans

    def numDecodings(self, s: str) -> int:
        if s == "0" or s == "":
            return 0

        return self.decode_with_memo(0, s)


# Approach 2: Iterative Approach
# Time: O(N)
# Space: O(N)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]
                if i + 1 < n and s[i : i + 2] <= "26":
                    dp[i] += dp[i + 2]

        return dp[0]


# Approach 3: Iterative Fibonacci Approach
# Time: O(N)
# Space: O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev1 = 1
        prev2 = 0
        curr = 0
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                curr = prev1
                if i + 1 < n and s[i : i + 2] <= "26":
                    curr += prev2
            prev2 = prev1
            prev1 = curr

        return curr
