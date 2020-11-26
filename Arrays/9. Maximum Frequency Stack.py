# https://leetcode.com/problems/maximum-frequency-stack/

"""
Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.
"""

import collections


class FreqStack(object):
    def __init__(self):
        self.frequencies = collections.Counter()  # counter of frequencies {'x':freq}
        self.freq_groups = collections.defaultdict(list)  # {'1':[1,2,3], '2':[2,1]}
        self.max_freq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        freq = self.frequencies[x] + 1
        self.frequencies[x] = freq
        self.max_freq = max(self.max_freq, freq)
        self.freq_groups[freq].append(x)

    def pop(self):
        """
        :rtype: int
        """
        element = self.freq_groups[self.max_freq].pop()
        self.frequencies[element] -= 1
        if not self.freq_groups[self.max_freq]:
            self.max_freq -= 1
        return element


# Heap
class FreqStack:
    def __init__(self):
        self.heap = []
        self.m = collections.defaultdict(int)
        self.counter = 0

    def push(self, x):
        self.m[x] += 1
        heapq.heappush(self.heap, (-self.m[x], -self.counter, x))
        self.counter += 1

    def pop(self):
        toBeRemoved = heapq.heappop(self.heap)
        self.m[toBeRemoved[2]] -= 1
        return toBeRemoved[2]


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()