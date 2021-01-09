# https://leetcode.com/problems/decode-ways-ii/


# DFS with memoization
# Time: O(N) since we decode each index once
# Space: O(N) since the memoization set would contain indecies up to len(s). same for recursion stack too
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [None] * len(s)
        M = 1000000007

        def ways(i):
            if i < 0:
                return 1
            if memo[i]:
                return memo[i]
            if s[i] == "*":
                # possibilities for signle digit combinations from 1 to 9
                res = 9 * ways(i - 1)
                # possibilities for double digit letters from 11 to 26
                if i > 0 and s[i - 1] == "1":
                    res = (res + 9 * ways(i - 2)) % M  # from 11 to 19
                elif i > 0 and s[i - 1] == "2":
                    res = (res + 6 * ways(i - 2)) % M  # from 21 to 26
                elif i > 0 and s[i - 1] == "*":
                    res = (res + 15 * ways(i - 2)) % M  # from 11 to 19 and from 21 to 26
                memo[i] = res
                return memo[i]

            # possibilities if the current letter is not *
            res = 0 if s[i] == "0" else ways(i - 1)
            # possibilities for double digit letters from 11 to 26
            if i > 0 and s[i - 1] == "1":  # from 11 to 19
                res = (res + ways(i - 2)) % M
            elif i > 0 and s[i - 1] == "2" and s[i] <= "6":  # from 21 to 26
                res = (res + ways(i - 2)) % M
            elif i > 0 and s[i - 1] == "*":  # *(1-9)
                # if s[i] <= '6', then we can have number between 11 to 16 and 21 to 26.
                # so double the possibilities
                factor = 2 if s[i] <= "6" else 1
                res = (res + factor * ways(i - 2)) % M

            memo[i] = res
            return memo[i]

        return ways(len(s) - 1)


# DP
# Time: O(N) since we decode each index once
# Space: O(N) since the memoization set would contain indecies up to len(s). same for recursion stack too
class Solution:
    def numDecodings(self, s: str) -> int:
        M = 1000000007
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 9 if s[0] == "*" else 0 if s[0] == "0" else 1
        for i in range(1, len(s)):
            if s[i] == "*":
                dp[i + 1] = 9 * dp[i]
                if s[i - 1] == "1":
                    dp[i + 1] = (dp[i + 1] + 9 * dp[i - 1]) % M
                elif s[i - 1] == "2":
                    dp[i + 1] = (dp[i + 1] + 6 * dp[i - 1]) % M
                elif s[i - 1] == "*":
                    dp[i + 1] = (dp[i + 1] + 15 * dp[i - 1]) % M
            else:
                dp[i + 1] = 0 if s[i] == "0" else dp[i]
                if s[i - 1] == "1":
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % M
                elif s[i - 1] == "2" and s[i] <= "6":
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % M
                elif s[i - 1] == "*":
                    factor = 2 if s[i] <= "6" else 1
                    dp[i + 1] = (dp[i + 1] + factor * dp[i - 1]) % M

        return dp[len(s)]


# DP with constant space (Iterative Fibonacci Approach)
# Time: O(N)
# Space: O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        M = 1000000007
        first = 1
        second = 9 if s[0] == "*" else 0 if s[0] == "0" else 1
        for i in range(1, len(s)):
            temp = second
            if s[i] == "*":
                second = 9 * second
                if s[i - 1] == "1":
                    second = (second + 9 * first) % M
                elif s[i - 1] == "2":
                    second = (second + 6 * first) % M
                elif s[i - 1] == "*":
                    second = (second + 15 * first) % M
            else:
                second = 0 if s[i] == "0" else second
                if s[i - 1] == "1":
                    second = (second + first) % M
                elif s[i - 1] == "2" and s[i] <= "6":
                    second = (second + first) % M
                elif s[i - 1] == "*":
                    factor = 2 if s[i] <= "6" else 1
                    second = (second + factor * first) % M
            first = temp

        return second


# https://leetcode.com/problems/decode-ways-ii/discuss/105274/Python-Straightforward-with-Explanation
# https://cs.stackexchange.com/questions/99513/dynamic-programming-vs-memoization