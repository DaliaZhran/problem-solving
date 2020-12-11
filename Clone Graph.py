# https://leetcode.com/problems/clone-graph/

# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# DFS
class Solution(object):
    visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        cloned_node = Node(node.val, [])
        self.visited[node] = cloned_node

        for neighbor in node.neighbors:
            cloned_node.neighbors.append(self.cloneGraph(neighbor))

        return cloned_node


# BFS
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node
        queue = deque([node])
        visited = {}
        visited[node] = Node(node.val, [])

        while queue:
            curr_node = queue.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])  # cloned node
                    queue.append(neighbor)

                visited[curr_node].neighbors.append(visited[neighbor])

        return visited[node]

