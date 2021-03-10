# https://leetcode.com/problems/palindrome-partitioning-ii/

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


# Brute Force
# Time: O(n * 2^n), where n is legnth of s
# Space: O(n)
class Solution:
    def minCut(self, s: str) -> int:
        def helper(start, end):
            if start == n or self.isPalindrome(s, start, end):
                return 0

            min_cut = end - start
            for i in range(start, end + 1):
                if self.isPalindrome(s, start, i):
                    min_cut = min(min_cut, 1 + helper(i + 1, end))
            return min_cut

        n = len(s)
        return helper(0, n - 1)

    def isPalindrome(self, s, start, end):
        while start <= end and s[start] == s[end]:
            start += 1
            end -= 1

        return start >= end


# Top-down Dynamic Programming with Memoization -> TLE
# Time: O(n * 2^n), where n is legnth of s
# Space: O(n^2)
class Solution:
    def minCut(self, s: str) -> int:
        def helper(start, end):
            if start == n or self.isPalindrome(s, start, end):
                return 0

            if dp[start][end] != -1:
                return dp[start][end]

            min_cut = end - start
            for i in range(start, end + 1):
                if self.isPalindrome(s, start, i):
                    min_cut = min(min_cut, 1 + helper(i + 1, end))

            dp[start][end] = min_cut
            return min_cut

        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        return helper(0, n - 1)

    def isPalindrome(self, s, start, end):
        while start <= end and s[start] == s[end]:
            start += 1
            end -= 1

        return start >= end


# Top-down Dynamic Programming with Memoization -> Accepted -> added dp matrix for checking palindrome too
# Time: O(n * 2^n), where n is legnth of s
# Space: O(n^2)
class Solution:
    def minCut(self, s: str) -> int:
        def helper(start, end):
            if start == n or self.isPalindrome(is_palindrome, s, start, end):
                return 0

            if dp[start][end] != -1:
                return dp[start][end]

            min_cut = end - start
            for i in range(start, end + 1):
                if self.isPalindrome(is_palindrome, s, start, i):
                    min_cut = min(min_cut, 1 + helper(i + 1, end))

            dp[start][end] = min_cut
            return min_cut

        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        is_palindrome = [[-1] * n for _ in range(n)]
        return helper(0, n - 1)

    def isPalindrome(self, is_palindrome, s, start, end):
        if is_palindrome[start][end] == -1:
            is_palindrome[start][end] = 1
            i, j = start, end
            while i < j:
                if s[i] != s[j]:
                    is_palindrome[start][end] = 0
                    break
                i += 1
                j -= 1
                if i < j and is_palindrome[i][j] != -1:
                    is_palindrome[start][end] = is_palindrome[i][j]
                    break

        return True if is_palindrome[start][end] == 1 else False


# Bottom-up Dynamic Programming
# Time: O(n^2), where n is legnth of s
# Space: O(n^2)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True

        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    if end - start == 1 or is_palindrome[start + 1][end - 1]:
                        is_palindrome[start][end] = True

        cuts = [0] * n
        for start in range(n - 1, -1, -1):
            min_cuts = n
            for end in range(n - 1, start - 1, -1):
                if is_palindrome[start][end]:
                    min_cuts = 0 if end == n - 1 else min(min_cuts, 1 + cuts[end + 1])

            cuts[start] = min_cuts

        return cuts[0]


# https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space.

# https://www.youtube.com/watch?v=lDYIvtBVmgo
