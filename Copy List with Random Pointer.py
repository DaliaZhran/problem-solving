# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

"""


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# * Approach 1 : Recursive
# Time : O(N)
# Space : O(N)
class Solution:
    visited = {}

    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return head

        if head in self.visited:
            return self.visited[head]

        cloned_node = Node(head.val)
        self.visited[head] = cloned_node

        cloned_node.next = self.copyRandomList(head.next)
        cloned_node.random = self.copyRandomList(head.random)

        return cloned_node


# * Approach 2 : Iterative/Queue
# Time : O(N)
# Space : O(N)
class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return head
        queue = deque([head])
        visited = {}
        visited[head] = Node(head.val)

        while queue:
            curr_node = queue.popleft()
            if curr_node.next and curr_node.next not in visited:
                visited[curr_node.next] = Node(curr_node.next.val)
                queue.append(curr_node.next)

            if curr_node.random and curr_node.random not in visited:
                visited[curr_node.random] = Node(curr_node.random.val)
                queue.append(curr_node.random)

            visited[curr_node].next = None if not curr_node.next else visited[curr_node.next]
            visited[curr_node].random = None if not curr_node.random else visited[curr_node.random]

        return visited[head]


# * Approach 2 : Iterative - No Queue
# Time : O(N)
# Space : O(N)
class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return head
        visited = {}
        old_node = head
        cloned_node = Node(head.val)
        visited[old_node] = cloned_node

        while old_node:
            if old_node.next and old_node.next not in visited:
                visited[old_node.next] = Node(old_node.next.val)

            if old_node.random and old_node.random not in visited:
                visited[old_node.random] = Node(old_node.random.val)

            cloned_node.next = None if not old_node.next else visited[old_node.next]
            cloned_node.random = None if not old_node.random else visited[old_node.random]

            cloned_node = cloned_node.next
            old_node = old_node.next

        return visited[head]



# * Approach 2 : Iterative - same as above but with modularity
# Time : O(N)
# Space : O(N)
class Solution(object):
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary          
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head

        old_node = head
        # Creating the new head node.       
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]