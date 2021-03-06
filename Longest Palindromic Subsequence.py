# https://leetcode.com/problems/longest-palindromic-subsequence/

'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
'''

# Brute Force - Recursive
# Time: O(2^n) where n is length of s
# Space: O(n)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def palindromeLength(start_idx, end_idx):
            if start_idx > end_idx:
                return 0
        
            if start_idx == end_idx:
                return 1
            
            if s[start_idx] == s[end_idx]:
                return 2 + palindromeLength(start_idx + 1, end_idx - 1)
            
            op2 = palindromeLength(start_idx + 1, end_idx)
            op3 = palindromeLength(start_idx, end_idx - 1)        
            return max(op2, op3)
        
        n = len(s)
        return palindromeLength(0, n - 1)



# Top Down Memoization
# Time: O(n^2) where n is length of s
# Space: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def palindromeLength(start_idx, end_idx):
            if start_idx > end_idx:
                return 0
            
            if dp[start_idx][end_idx] != 0:
                return dp[start_idx][end_idx]
            
            if start_idx == end_idx:
                return 1
            
            if s[start_idx] == s[end_idx]:
                dp[start_idx][end_idx] = 2 + palindromeLength(start_idx + 1, end_idx - 1)
            else:
                op2 = palindromeLength(start_idx + 1, end_idx)
                op3 = palindromeLength(start_idx, end_idx - 1)
                dp[start_idx][end_idx] = max(op2, op3)
                
            return dp[start_idx][end_idx]
        
        
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        return palindromeLength(0, n - 1)
    

# Bottom Up DP
# Time: O(n^2) where n is length of s
# Space: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for start_idx in range(n - 1, -1, -1):
            for end_idx in range(start_idx + 1, n):
                if s[start_idx] == s[end_idx]:
                    dp[start_idx][end_idx] = 2 + dp[start_idx + 1][end_idx - 1]
                else:
                    dp[start_idx][end_idx] = max(dp[start_idx + 1][end_idx], dp[start_idx][end_idx - 1])        
                    
        return dp[0][-1]
    


# Bottom Up DP - but going down diagonally
# Time: O(n^2) where n is length of s
# Space: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for curr_len in range(2, n + 1): # check every palindormic length
            for i in range(0 , n - curr_len + 1):
                j = i + curr_len - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])        
                    
        return dp[0][-1]
    


# Reducing Space
# Time: O(n^2) where n is length of s
# Space: O(n)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        prev_row = [0] * n
        prev_row[-1] = 1
        for start_idx in range(n - 1, -1, -1):
            curr_row = [0] * n
            curr_row[start_idx] = 1
            for end_idx in range(start_idx + 1, n):
                if s[start_idx] == s[end_idx]:
                    curr_row[end_idx] = 2 + prev_row[end_idx - 1]
                else:
                    curr_row[end_idx] = max(prev_row[end_idx], curr_row[end_idx - 1]) 
            
            prev_row = curr_row
                    
        return curr_row[-1]