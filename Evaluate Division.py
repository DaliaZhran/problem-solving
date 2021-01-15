# https://leetcode.com/problems/evaluate-division/

"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction. 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

"""

# DFS
# Time : O(M*N)
# Space : O(N)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildGraph(equations, values)
        res = []
        for query in queries:
            product = self.pathWeight(query[0], query[1], set(), graph)
            res.append(product)
        return res

    def buildGraph(self, edges, weights):
        graph = defaultdict(defaultdict)
        for (source, destination), weight in zip(edges, weights):
            graph[source][destination] = weight
            graph[destination][source] = 1 / weight
        return graph

    def pathWeight(self, start_node, target_node, visited, graph):
        if start_node not in graph:
            return -1
        if target_node in graph[start_node]:
            return graph[start_node][target_node]

        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                visited.add(node)
                product = self.pathWeight(node, target_node, visited, graph)
                if product != -1:
                    return product * graph[start_node][node]
        return -1


# https://leetcode.com/problems/evaluate-division/discuss/88275/Python-fast-BFS-solution-with-detailed-explantion