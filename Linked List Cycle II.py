# https://leetcode.com/problems/linked-list-cycle-ii/

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
"""

# Approach 1: keep track of all items in set

# Approach 2: hare and tortoise

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# time -> O(n)
# space -> O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break

        if not fast or not fast.next:  # no cycle
            return None

        # get len of cycle
        slow = slow.next
        length = 1
        while slow != fast:
            slow = slow.next
            length += 1

        slow, fast = head, head
        while length:
            fast = fast.next
            length -= 1

        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


# another implementation
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None
