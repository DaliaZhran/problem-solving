# https://leetcode.com/problems/reverse-nodes-in-k-group/

"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative
# Time : O(N)
# Space : O(1)
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ptr = head
        ktail = None
        # Head of the final, moified linked list
        new_head = None

        # Keep going until there are no nodes in the list
        while ptr:
            # count k nodes from the current head
            count = 0
            ptr = head
            while count < k and ptr:
                ptr = ptr.next
                count += 1

            # If we counted k nodes, reverse them
            if count == k:
                # Reverse k nodes and get the new head
                rev_head = self.reverseList(head, k)

                if not new_head:
                    new_head = rev_head

                if ktail:
                    ktail.next = rev_head

                ktail = head
                # next head is the one after the end of the current k nodes list
                head = ptr

        # attach the final, possibly un-reversed portion
        if ktail:
            ktail.next = head

        return new_head if new_head else head

    def reverseList(self, head: ListNode, k: int) -> ListNode:
        prev = None
        curr = head
        while k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k -= 1
        return prev


# Recursive
# Time : O(N)
# Space : O(N)
# https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11423/Short-but-recursive-Java-code-with-commentss