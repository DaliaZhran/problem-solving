# https://leetcode.com/problems/reverse-string/

"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

# Recursive
# Time : O(N)
# Space : O(N) for the recursive stack
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def helper(left, right):
            if left >= right:
                return
            helper(left + 1, right - 1)
            s[left], s[right] = s[right], s[left]

        helper(0, len(s) - 1)


# Iterative
# Time : O(N)
# Space : O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
