# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/


# Graph - Similar Idea to Topological Sorting
# Time: O(N)
# Space: O(N)
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        G = defaultdict(list)

        for n1, n2 in adjacentPairs:
            G[n1].append(n2)
            G[n2].append(n1)

        to_visit = []
        for n in G:
            if len(G[n]) == 1:
                to_visit.append((n, None))
                break

        res = []
        while to_visit:
            node, parent = to_visit.pop()
            res.append(node)
            for num in G[node]:
                if num != parent:
                    to_visit.append((num, node))

        return res