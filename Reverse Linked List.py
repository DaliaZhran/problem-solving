# https://leetcode.com/problems/reverse-linked-list/

"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# * iterative
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev = head
        curr = head.next
        head.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        curr = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return curr
