# https://leetcode.com/problems/critical-connections-in-a-network/


# Tarjan's Algorithm
# Time : O(V + E)
# Space : O(E)
class Solution:
    time = 1

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(n, connections)
        disc = [-1] * n  # discovery time
        low = [-1] * n  # earlist accessible node from the current node
        parent = [-1] * n  # parent of each node
        critical_edges = []  # result
        for i in range(n):
            if disc[i] == -1:
                self.dfs(i, graph, disc, low, parent, critical_edges)

        return critical_edges

    def dfs(self, u, graph, disc, low, parent, critical_edges):
        disc[u] = low[u] = self.time
        self.time += 1
        for v in graph[u]:
            parent[v] = u
            if v == parent[u]:
                continue
            if disc[v] == -1:
                self.dfs(v, graph, disc, low, parent, critical_edges)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    critical_edges.append([u, v])
            else:
                low[u] = min(low[u], disc[v])

    def build_graph(self, n, connections):
        graph = [[] for _ in range(n)]
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        return graph


# Same solution but removed the parent array and just pass the parent as a parameter
class Solution:
    time = 1

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = self.build_graph(n, connections)
        disc = [-1] * n  # discovery time
        low = [-1] * n  # earlist accessible node from the current node
        critical_edges = []  # result
        for i in range(n):
            if disc[i] == -1:
                self.dfs(i, graph, disc, low, -1, critical_edges)

        return critical_edges

    def dfs(self, u, graph, disc, low, u_parent, critical_edges):
        disc[u] = low[u] = self.time
        self.time += 1
        for v in graph[u]:
            if v == u_parent:
                continue
            if disc[v] == -1:
                self.dfs(v, graph, disc, low, u, critical_edges)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:
                    critical_edges.append([u, v])
            else:
                low[u] = min(low[u], disc[v])

    def build_graph(self, n, connections):
        graph = [[] for _ in range(n)]
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        return graph


# https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/DFS-detailed-explanation-O(orEor)-solution
# https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me