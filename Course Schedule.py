# https://leetcode.com/problems/course-schedule/
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""

from collections import deque, defaultdict

# my sol -> Kahn Algorithm
# time ->
# space ->
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
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

        while noDependencyCourses:  # decrement indegree of dependend course on finished courses
            node = noDependencyCourses.pop()
            for course in G[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    noDependencyCourses.append(course)

        for i in indegree:  # check if all were finished
            if i != 0:
                return False
        return True


# small edit -> removed last loop by using a variable
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        G = [[] for i in range(numCourses)]  # adj. list representation
        indegree = [0] * numCourses

        edges = 0
        for nextCourse, prevCourse in prerequisites:  # edges are switched in the problem desc
            G[prevCourse].append(nextCourse)  # create the adj list
            indegree[nextCourse] += 1
            edges += 1

        noDependencyCourses = deque([])  # no dependency courses
        for i in range(numCourses):  # can use comperehention here
            if indegree[i] == 0:
                noDependencyCourses.append(i)

        while noDependencyCourses:
            node = noDependencyCourses.pop()
            for course in G[node]:
                indegree[course] -= 1
                edges -= 1
                if indegree[course] == 0:
                    noDependencyCourses.append(course)

        # for i in indegree:
        #     if i != 0:
        #         return False
        return edges == 0


# solution using Graph node class -> leetcode sol
class GNode(object):
    """  data structure represent a vertex in the graph."""

    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # key: index of node; value: GNode
        graph = defaultdict(GNode)

        totalDeps = 0
        for nextCourse, prevCourse in prerequisites:
            graph[prevCourse].outNodes.append(nextCourse)
            graph[nextCourse].inDegrees += 1
            totalDeps += 1

        # we start from courses that have no prerequisites.
        # we could use either set, stack or queue to keep track of courses with no dependence.
        nodepCourses = deque()
        for index, node in graph.items():
            if node.inDegrees == 0:
                nodepCourses.append(index)

        removedEdges = 0
        while nodepCourses:
            # pop out course without dependency
            course = nodepCourses.pop()

            # remove its outgoing edges one by one
            for nextCourse in graph[course].outNodes:
                graph[nextCourse].inDegrees -= 1
                removedEdges += 1
                # while removing edges, we might discover new courses with prerequisites removed, i.e. new courses without prerequisites.
                if graph[nextCourse].inDegrees == 0:
                    nodepCourses.append(nextCourse)

        if removedEdges == totalDeps:
            return True
        else:
            # if there are still some edges left, then there exist some cycles
            # Due to the dead-lock (dependencies), we cannot remove the cyclic edges
            return False


# sol -> DFS -> nice to know
def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in xrange(numCourses)]
    visit = [0 for _ in xrange(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y)

    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True

    for i in xrange(numCourses):
        if not dfs(i):
            return False
    return True


# if node v has not been visited, then mark it as 0.
# if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
# if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
