# https://leetcode.com/problems/reorder-list/

"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        secondHalf = reverse(slow)
        firstHalf = head
        while firstHalf and secondHalf:
            # exchange as zigzag
            temp = firstHalf.next
            firstHalf.next = secondHalf
            firstHalf = temp

            temp = secondHalf.next
            secondHalf.next = firstHalf
            secondHalf = temp

        # if list length is even, last element of second half next would be itself (cycle), so we remove this next pointer
        if firstHalf != None:  # if last element is from first half, then remove the next pointer
            firstHalf.next = None


def reverse(head):
    prev = None
    while head != None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev
