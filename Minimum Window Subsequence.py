# https://leetcode.com/problems/minimum-window-subsequence/

"""
Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:

Input: 
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation: 
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.
"""

# Two Pointers
# Time : T(m+(# of pattern found)*n) which in worse case O(mn).
# Space : O(1)
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        s_len, t_len = len(S), len(T)
        min_win_len = float("inf")
        result = ""
        win_end = 0

        while win_end < s_len:
            t_index = 0
            while win_end < s_len:
                if S[win_end] == T[t_index]:
                    t_index += 1
                if t_index == t_len:
                    break
                win_end += 1

            if win_end == s_len:
                break

            win_start = win_end
            t_index = t_len - 1
            while win_start >= 0:
                if S[win_start] == T[t_index]:
                    t_index -= 1
                if t_index < 0:
                    break
                win_start -= 1

            if win_end - win_start + 1 < min_win_len:
                min_win_len = win_end - win_start + 1
                result = S[win_start : win_end + 1]

            win_end = win_start + 1

        return result


# DP
# https://leetcode.com/problems/minimum-window-subsequence/discuss/109354/Python-O(m)-space-complexity-almost-O(n)-time-complexity