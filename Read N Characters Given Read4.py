# https://leetcode.com/problems/read-n-characters-given-read4/

"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

# time -> O(n)
# space -> O(4) -> O(1)
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        read_chars_total = 0
        iterations = n // 4 + 1 if n % 4 else n // 4
        temp_buf = [""] * 4
        for i in range(iterations):
            read_chars_num = read4(temp_buf)
            for j in range(min(read_chars_num, n)):
                buf[i * 4 + j] = temp_buf[j]
                read_chars_total += 1
            n -= read_chars_num
        return read_chars_total


# better implementation
# time -> O(n)
# space -> O(4) -> O(1)
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        buf_ptr = 0
        read_cnt = 4
        temp_buf = [""] * 4
        while buf_ptr < n and read_cnt == 4:
            temp_read_cnt = read4(temp_buf)
            for j in range(temp_read_cnt):
                buf[buf_ptr] = temp_buf[j]
                buf_ptr += 1
                if buf_ptr == n:
                    break
            read_cnt = temp_read_cnt
        return buf_ptr