# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time : O(N)
# Space: O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = res = ListNode(-200, head)
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr and curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return res.next
