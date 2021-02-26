# https://leetcode.com/problems/find-the-celebrity/

"""
Suppose you are at a party with n people (labeled from 0 to n - 1), and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her, but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
"""

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


# Brute Force
# Time: O(n^2) -> assuming knows function is O(1) just for the sake of knowing our algorithm complexity
# Space: O(1)
class Solution:
    def findCelebrity(self, n: int) -> int:
        for i in range(n):
            for j in range(n):
                if i != j and knows(i, j) or not knows(j, i):
                    break
            else:
                return i
        return -1


# Another Implementation
class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n = n
        for i in range(n):
            if self.is_celebrity(i):
                return i
        return -1

    def is_celebrity(self, i):
        for j in range(self.n):
            if i == j:
                continue  # Don't ask if they know themselves.
            if knows(i, j) or not knows(j, i):
                return False
        return True


# Approach 2: Logical Deduction
# Time: O(n)
# Space: O(1)
class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        if self.is_celebrity(n, candidate):
            return candidate
        return -1

    def is_celebrity(self, n, candidate):
        for j in range(n):
            if candidate == j:
                continue
            if knows(candidate, j) or not knows(j, candidate):
                return False
        return True


# Check fine tunings