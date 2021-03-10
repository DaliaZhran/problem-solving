# https://leetcode.com/problems/palindrome-partitioning-iv/discuss/?currentPage=1&orderBy=most_votes&query=


# Brute Force -> TLE
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def helper(start, count):
            if count == 2 and self.isPalindrome(is_palindrome, s, start, n - 1):
                return True

            if start == n:
                return False

            for i in range(start, n):
                if self.isPalindrome(is_palindrome, s, start, i):
                    if helper(i + 1, count + 1):
                        return True

            return False

        n = len(s)
        is_palindrome = [[-1] * n for _ in range(n)]
        return helper(0, 0)

    def isPalindrome(self, is_palindrome, s, start, end):
        if start > end:
            return False
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


# Top-down Dynamic Programming with Memoization
# start and counting are the changing parameters so we can apply memoization
