# https://leetcode.com/problems/task-scheduler/

"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
"""
from heapq import heappop, heappush
from collections import deque

# Time -> O(N)
# space -> O(1)
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq_map = {}
        for task in tasks:
            freq_map[task] = freq_map.get(task, 0) + 1

        max_heap = []
        for task, freq in freq_map.items():
            heappush(max_heap, (-freq, task))

        interval_cnt = 0
        while max_heap:
            wait_queue = deque()
            k = n + 1
            while k > 0 and max_heap:
                freq, task = heappop(max_heap)
                interval_cnt += 1
                if -freq > 1:
                    wait_queue.append((freq + 1, task))
                k -= 1

            # we add the rest of the items to the max heap if there are any
            # then we check if k > 0, we need to add idle intervals to the interval_cnt
            for freq, task in wait_queue:
                heappush(max_heap, (freq, task))

            if max_heap:
                interval_cnt += k

        return interval_cnt


# GREEDY
# Time -> O(N)
# space -> O(1)
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        frequencies = Counter(tasks)
        frequencies = [v for k, v in sorted(frequencies.items(), key=lambda item: item[1])]
        len_tasks = sum(frequencies)
        max_freq = frequencies.pop()
        idle_time = (max_freq - 1) * n

        while frequencies and idle_time > 0:
            idle_time -= min(max_freq - 1, frequencies.pop())  # we use the min now because we can get the max number more than once so we need to substract 1
        idle_time = max(0, idle_time)  # use max to check if there is idle time or not

        return idle_time + len_tasks


# Math
# Time -> O(N)
# space -> O(1)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord("A")] += 1

        # max frequency
        f_max = max(frequencies)
        # count the most frequent tasks
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)