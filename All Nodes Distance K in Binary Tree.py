# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# BFS -> convert tree to graph
# Time -> O(N) linear time for annotate_parent and the bfs search
# Space -> O(N) for queue, new_level, and seen
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parent_map = defaultdict(None)

        def annotate_parent(node, parent):
            if node:
                parent_map[node] = parent
                annotate_parent(node.left, node)
                annotate_parent(node.right, node)

        annotate_parent(root, None)

        queue = deque([target])
        seen = {target}
        for _ in range(K):
            new_level = []
            for node in queue:
                for neighbor in [node.left, node.right, parent_map[node]]:
                    if neighbor and neighbor not in seen:
                        seen.add(neighbor)
                        new_level.append(neighbor)

            queue = new_level

        return [x.val for x in queue]


# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/143798/1ms-beat-100-simple-Java-dfs-with(without)-hashmap-including-explanation