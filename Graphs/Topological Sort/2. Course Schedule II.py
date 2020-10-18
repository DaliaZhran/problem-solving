# https://leetcode.com/problems/course-schedule-ii/
"""
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""

from collections import deque, defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        G = [[] for i in range(numCourses)]  # adj. list representation
        indegree = [0] * numCourses

        for nextCourse, prevCourse in prerequisites:  # edges are switched in the problem desc
            G[prevCourse].append(nextCourse)  # create the adj list
            indegree[nextCourse] += 1

        noDependencyCourses = deque([])  # no dependency courses
        for i in range(numCourses):  # can use comperehention here
            if indegree[i] == 0:
                noDependencyCourses.append(i)

        iterator = 0
        while iterator < len(noDependencyCourses):  # decrement indegree of dependend course on finished courses
            node = noDependencyCourses[iterator]
            for course in G[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    noDependencyCourses.append(course)
            iterator += 1

        if len(noDependencyCourses) == numCourses:
            return noDependencyCourses
        return []


# simple modification -> use a list to keep track of sorted courses instead of iterator
# time -> O(V+E)  where V represents the number of vertices and E represents the number of edges.
# space -> O(V+E) where V represents the number of vertices and E represents the number of edges.
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        G = [[] for i in range(numCourses)]  # adj. list representation
        indegree = [0] * numCourses

        for nextCourse, prevCourse in prerequisites:  # edges are switched in the problem desc
            G[prevCourse].append(nextCourse)  # create the adj list
            indegree[nextCourse] += 1

        noDependencyCourses = deque([])  # no dependency courses
        for i in range(numCourses):  # can use comperehention here
            if indegree[i] == 0:
                noDependencyCourses.append(i)

        sortedCourses = []
        while noDependencyCourses:  # decrement indegree of dependend course on finished courses
            node = noDependencyCourses.pop()
            sortedCourses.append(node)
            for course in G[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    noDependencyCourses.append(course)

        if len(sortedCourses) == numCourses:
            return sortedCourses
        return []


# DFS
# time -> O(N)
# space -> O(N)
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        def dfs(node):
            if visited[node] == -1:
                return False
            elif visited[node] == 1:
                return True

            visited[node] = -1
            for adjNode in graph[node]:
                if not dfs(adjNode):
                    return False
            visited[node] = 1
            sorted_order.append(node)
            return True

        graph = [[] for i in range(numCourses)]  # adj. list representation
        visited = [0] * numCourses
        sorted_order = []

        for nextCourse, prevCourse in prerequisites:  # edges are switched in the problem desc
            graph[prevCourse].append(nextCourse)  # create the adj list

        for node in range(numCourses):
            if not dfs(node):
                return []
        return sorted_order[::-1]
