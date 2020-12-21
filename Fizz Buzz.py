# https://leetcode.com/problems/fizz-buzz/

"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [0] * n
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res[i - 1] = "FizzBuzz"
            elif i % 3 == 0:
                res[i - 1] = "Fizz"
            elif i % 5 == 0:
                res[i - 1] = "Buzz"
            else:
                res[i - 1] = str(i)
        return res
