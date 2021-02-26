# https://leetcode.com/problems/utf-8-validation/

"""
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:
- For 1-byte character, the first bit is a 0, followed by its unicode code.
- For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.

This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
"""

# Implementation problem so try to think abt the algorithm first

# Bit Manipulation
# Time: O(N)
# Space: O(1)
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        i = 0
        while i < n:
            # get number of utf bytes
            num_of_bytes = self.count_ones(data[i])
            if num_of_bytes == 1 or num_of_bytes > 4:
                return False
            if num_of_bytes == 0:
                i += 1
                continue

            i += 1
            num_of_bytes -= 1
            # skip the num of integers = num of bytes
            while i < n and num_of_bytes != 0:
                byte_start = self.count_ones(data[i])
                if byte_start == 1:
                    num_of_bytes -= 1
                    i += 1
                else:
                    return False

        return num_of_bytes == 0

    # counts most signficant ones
    def count_ones(self, num):
        count = 0
        j = 1 << 7
        while j & num:
            j = j >> 1
            count += 1
        return count