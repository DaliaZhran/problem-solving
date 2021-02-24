# https://leetcode.com/problems/2-keys-keyboard/

"""
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
 

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.
"""


# Brute Force -> Recursion
# Time: O(2^n)
# Space: O(n)
class Solution:
    def minSteps(self, n: int) -> int:
        def solve(on_screen, copied):
            if on_screen > n:
                return float("inf")
            if on_screen == n:
                return 0

            op1 = 2 + solve(on_screen + on_screen, on_screen)  # copy and paste option
            op2 = 1 + solve(on_screen + copied, copied)  # paste option

            return min(op1, op2)

        # solve after initially copying the A on the screen
        return 1 + solve(1, 1) if n > 1 else 0


# DP - Bottom Up
# Time: O(n)
# Space: O(n)
class Solution:
    def minSteps(self, n: int) -> int:
        def solve(on_screen, copied):
            if on_screen > n:
                return float("inf")
            if on_screen == n:
                return 0

            if (on_screen, copied) in dp:
                return dp[(on_screen, copied)]

            op1 = 2 + solve(on_screen + on_screen, on_screen)  # copy and paste option
            op2 = 1 + solve(on_screen + copied, copied)  # paste option

            dp[(on_screen, copied)] = min(op1, op2)

            return dp[(on_screen, copied)]

        # solve after initially copying the A on the screen
        dp = {}
        return 1 + solve(1, 1) if n > 1 else 0


# Time: O(n)
# Space: O(1)
class Solution:
    def minSteps(self, n: int) -> int:
        curr = 1
        count = 0
        memory = 0
        while curr < n:
            rest = n - curr
            if rest % curr == 0:  # corresponds to Copy and Paste
                memory = curr  # copy
                curr += memory  # paste
                count += 2
            else:  # corresponds to Paste
                curr += memory
                count += 1

        return count


# integer Factorization
# Explanation -> https://leetcode.com/problems/2-keys-keyboard/discuss/105910/Python-Integer-factorization
# Time: O(sqrt(N))
def minSteps(self, n):
    for i in xrange(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return self.minSteps(n / i) + i
    return 0 if n == 1 else n


# https://leetcode.com/problems/2-keys-keyboard/discuss/882351/Simple-Top-Down-Recursive-Log(n)-Solution-or-C%2B%2B-or-100
