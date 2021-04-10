# https://leetcode.com/problems/rotate-list/
"""
Given the head of a linked list, rotate the list to the right by k places.
"""


""" this gives run time error because we loop all the k (think if k is 200000) """
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time: O(max(k, n))
# class Solution(object):
#     def rotateRight(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
#         if not head or not k:
#             return head

#         slow, fast = head, head

#         for i in range(k):
#             if fast:
#                 fast = fast.next
#             else:
#                 fast = head.next

#         if not fast:
#             return head

#         while fast and fast.next:
#             fast = fast.next
#             slow = slow.next

#         temp = slow.next
#         slow.next = None
#         fast.next = head

#         return temp


""" This is a better solution -> O(n)"""

# time: O(N)
# Space: O(1)
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        k = k % length  # to avoid so many cycles and TLE error
        if k == 0:
            return head

        fast = slow = head
        while fast and k:
            fast = fast.next
            k -= 1

        while fast.next and slow:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None
        return head


# time: O(N)
# Space: O(1)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k:
            return head

        length = 1
        temp = head
        while temp.next:
            length += 1
            temp = temp.next

        k = k % length  # to avoid so many cycles
        if k == 0:
            return head

        # connect end of list to its head
        temp.next = head
        # split the k elements from end
        splitter = head
        for _ in range(length - k - 1):
            splitter = splitter.next
        # assign new head and tail
        head = splitter.next
        splitter.next = None
        return head
