# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative
# Time : O(N)
# Space : O(1)
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        curr = head
        prev = None
        while m > 1 and curr:
            prev = curr
            curr = curr.next
            n -= 1
            m -= 1

        tail = curr
        discont_point = prev

        while n > 0:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1

        tail.next = curr
        if discont_point:
            discont_point.next = prev
        else:
            head = prev

        return head


# Same Idea -> better implementation
# https://leetcode.com/problems/reverse-linked-list-ii/discuss/30709/Talk-is-cheap-show-me-the-code-(and-DRAWING)