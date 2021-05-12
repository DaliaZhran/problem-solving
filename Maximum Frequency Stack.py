# https://leetcode.com/problems/maximum-frequency-stack/

"""
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
"""
from collections import defaultdict
from heapq import heappop, heappush


# using stack for each frequency
# space: O(n + m) where n -> number of values pushed, m -> max number of occurences of one number
class FreqStack:
    def __init__(self):
        self.frequencies_mp = defaultdict(list)  # {'1':[1,2,3], '2':[2,1]}
        self.nums_mp = defaultdict(int)  # counter of frequencies {'x':freq}
        self.top_freq = 0

    # time: O(1)
    def push(self, val: int) -> None:
        num_freq = self.nums_mp[val] + 1
        self.nums_mp[val] = num_freq
        self.top_freq = max(self.top_freq, num_freq)
        self.frequencies_mp[num_freq].append(val)

    # time: O(1)
    def pop(self) -> int:
        val = self.frequencies_mp[self.top_freq].pop()
        self.nums_mp[val] -= 1
        if self.frequencies_mp[self.top_freq] == []:
            self.top_freq -= 1
        return val


# Heap (freq, order, value)
class FreqStack:
    def __init__(self):
        self.heap = []
        self.m = defaultdict(int)
        self.counter = 0  # order

    # time: O(log(n))
    def push(self, x):
        self.m[x] += 1
        heappush(self.heap, (-self.m[x], -self.counter, x))
        self.counter += 1

    # time: O(log(n))
    def pop(self):
        _, _, x = heappop(self.heap)
        self.m[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
