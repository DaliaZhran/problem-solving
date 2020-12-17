# https://leetcode.com/explore/interview/card/google/59/array-and-strings/436/


# The read4 API is already defined for you.
# @param buf4, List[str]
# @return an integer
# def read4(buf4):


class Solution(object):
    temp_buf_ptr = 0  # points to the current index of the temp buffer
    temp_buf_cnt = 0  # number of chars in the temp buffer
    temp_buf = [""] * 4

    def read(self, buf, n):
        """
        :type buf: List[str]
        :type n: int
        :rtype: int
        """
        curr_cnt = 0
        while curr_cnt < n:
            if self.temp_buf_ptr == self.temp_buf_cnt:  # if nothing in the temp buffer or all chars are already copied, read from file
                self.temp_buf_cnt = read4(self.temp_buf)
                self.temp_buf_ptr = 0
            if self.temp_buf_cnt == 0:  # if there is nothing more to read/copy, then stop
                break
            while curr_cnt < n and self.temp_buf_ptr < self.temp_buf_cnt:  # copy chars from temp buffer to output buf
                buf[curr_cnt] = self.temp_buf[self.temp_buf_ptr]
                curr_cnt += 1
                self.temp_buf_ptr += 1

        return curr_cnt


# * we can replace the buffer with a queue to avoid the headache and compexity of using temp_buf_cnt and temp_buf_ptr
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/193873/Most-elegant-and-simple-solution-in-Python

## * Follow Up: -> cannot be done in python though since there are no pointers in python
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/188293/Google-follow-up-question.-Speed-up-the-copy.