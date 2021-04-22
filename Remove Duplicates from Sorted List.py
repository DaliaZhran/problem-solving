# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Time: O(N)
# Space: O(1)
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = head
        while cur != None:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head


# Time: O(N)
# Space: O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = res = ListNode(-200)
        curr = head
        while curr:
            if prev.val != curr.val:
                prev.next = curr
                prev = prev.next
            curr = curr.next
        prev.next = None
        return res.next


# better implementation
# Time: O(N)
# Space: O(1)
def deleteDuplicates(self, head):
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head
