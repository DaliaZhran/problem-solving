# https://leetcode.com/problems/palindrome-permutation/

"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
"""

# time -> O(n)
# space -> O(1)
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = Counter(s)
        flag = 0
        for ch, freq in count.items():
            if freq % 2 != 0:
                flag += 1
                if flag > 1:
                    return False
        return True
