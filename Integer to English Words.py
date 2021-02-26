#  https://leetcode.com/problems/integer-to-english-words/

"""
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

"""


# Divide and Conquer -> think before implementation
# Time: O(N)
# Space: O(1)
class Solution:

    LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        words = ""
        i = 0
        while num:
            if num % 1000 != 0:
                words = self.convert(num % 1000) + self.THOUSANDS[i] + " " + words
            num = num // 1000
            i += 1

        return words.strip()

    def convert(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.LESS_THAN_20[num] + " "
        elif num < 100:
            return self.TENS[num // 10] + " " + self.convert(num % 10)
        else:
            return self.LESS_THAN_20[num // 100] + " Hundred " + self.convert(num % 100)
        # we can continue with < 1M and < 1B too and avoid the while loop in numberToWords function
