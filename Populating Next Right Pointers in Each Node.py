# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# BFS -> Not constant memory -> sentinel node
# time O(n)
# space O(n) for queue
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


# intuitive BFS: level order solution -> faster a little bit
# time O(n)
# space O(n) queue
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
            newlevel = []
            node = queue.popleft()
            for i in queue:
                node.next = i
                if node.left:
                    newlevel.append(node.left)
                if node.right:
                    newlevel.append(node.right)
                node = node.next

            if node.left:
                newlevel.append(node.left)
            if node.right:
                newlevel.append(node.right)
            node.next = None
            queue = deque(newlevel)

        return root


# better intuitive solution
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


# best solution -> Iterative
# time O(n)
# space O(1)
class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None

        leftmost = root

        # if leftmost.left is none, then we are in the last level which is already connected because it is a perfect binary tree
        while leftmost.left:
            head = leftmost
            while head:
                # connection 1
                head.left.next = head.right
                # connection 2
                if head.next:
                    head.right.next = head.next.left

                # go to next node in the same level
                head = head.next

            # go to the first node in the next level
            leftmost = leftmost.left

        return root


# Recursive
# time O(n)
# space O(1) since in the problem stack space is not counted
class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
