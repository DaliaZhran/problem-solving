# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Approach 1: Three Pass Approach -> get length first, then k node and n - k node, each in a loop
# Approach 2: Two Pass Approach -> get length and k node in one loop, then n-k node in another loop

# 1 pass approach
# Time : O(N)
# Space : O(1)
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        fast, slow = head, head
        i = 1
        while fast.next and i < k:
            fast = fast.next
            i += 1

        if not fast:
            return head

        kth_node_begin = fast

        while fast.next:
            fast = fast.next
            slow = slow.next

        kth_node_end = slow

        kth_node_begin.val, kth_node_end.val = kth_node_end.val, kth_node_begin.val

        return head