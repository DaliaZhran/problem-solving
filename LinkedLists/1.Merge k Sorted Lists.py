# https://leetcode.com/problems/merge-k-sorted-lists/

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6


from Queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Using priority queue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = dummy = ListNode(0)
        heap = PriorityQueue()

        for l in lists:
            if l:
                print(l)
                heap.put((l.val, l))
        while not heap.empty():
            val, node = heap.get()

            dummy.next = ListNode(val)
            dummy = dummy.next
            node = node.next
            if node:
                heap.put((node.val, node))

        return head.next

    # same with a little difference
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = dummy = ListNode(0)
        heap = PriorityQueue()

        for l in lists:
            while l:
                heap.put((l.val, l))
                l = l.next
        while not heap.empty():
            val, node = heap.get()

            dummy.next = ListNode(val)
            dummy = dummy.next
        #             node = node.next
        #             if node:
        #                 heap.put((node.val, node))

        return head.next
