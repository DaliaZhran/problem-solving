# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

# BFS
# time O(n) -> best
# space O(n)
class Solution(object):
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        queue = [root, None]
        while queue:
            node = queue.pop(0)
            if node:
                node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:  # this means we reached the end of a level (aka the children of that level are all added to the queue so we need to append None to end that children level)
                if queue:
                    queue.append(None)
        return root


# BFS
# time O(n) -> best
# space O(n)
class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i != level_size - 1:  # means we didnt still reach the end of the level and also no need for else because node.next by default is None
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


# BFS but no queue
# time O(n) -> best
# space O(1) -> best
class Solution(object):
    def processChild(self, child, prev, leftmost):
        if child:
            if prev:
                prev.next = child
            else:
                leftmost = child

            prev = child
        return prev, leftmost

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root

        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost
            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None

            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)

                curr = curr.next
        return root
