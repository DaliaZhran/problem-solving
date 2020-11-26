# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
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
            temp = firstHalf.next
            firstHalf.next = secondHalf
            firstHalf = temp

            temp = secondHalf.next
            secondHalf.next = firstHalf
            secondHalf = temp

        if firstHalf != None:
            firstHalf.next = None


def reverse(head):
    prev = None
    while head != None:
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    return prev
