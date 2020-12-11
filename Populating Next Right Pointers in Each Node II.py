# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Given a binary tree

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# BFS
# time O(n) -> best
# space O(n)
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
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
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        queue = deque([root])

        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()
                if i < levelSize - 1:  # means we didnt still reach the end of the level and also no need for else because node.next by default is None
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
        leftmost = root

        while leftmost:
            prev, curr = None, leftmost
            leftmost = None

            while curr:
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)

                curr = curr.next
        return root
