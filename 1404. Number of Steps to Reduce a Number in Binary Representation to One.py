# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

"""
Given a number s in their binary representation. Return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.

It's guaranteed that you can always reach to one for all testcases.

 

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  
"""


class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = int(s, 2)
        cnt = 0
        while num != 1:
            if num & 1:
                num += 1
            else:
                num >>= 1
            cnt += 1
        return cnt


# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/discuss/564287/C%2B%2BJava-O(n)
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/discuss/564323/Clean-Python-3-two-pointers-O(n)O(1)