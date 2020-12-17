# https://leetcode.com/problems/next-permutation/

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
"""


# Approach 1: Brute Force
# Time -> O(n!)
# Space -> O(n) Since an array will be used to store the permutations
