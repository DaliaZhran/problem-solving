# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Follow up: Could you do this in one pass?

Examples:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1,2,3,4,5], n = 5 # edge case
Output: [2,3,4,5]
"""

# Brute Force -> Get length of list, then remove element at L - N -> O(2N)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(N)
# Space: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head

        slow = fast = head
        while fast and n:
            fast = fast.next
            n -= 1

        if not fast:  # important edge case when head is to be removed
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
