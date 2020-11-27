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

        return head.next


# same idea, another implementation using heap
class Solution(object):
    # best implementation
    # space -> O(k) where k is the len(lists)
    # Time complexity : O(N log k)
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        head = dummy = ListNode(0)
        for l in lists:
            if l:  # add only first node since all lists are sorted, this decreases the space complexity
                heappush(min_heap, (l.val, l))
                l = l.next

        while min_heap:
            val, node = heappop(min_heap)
            temp = node.next
            node.next = None  # use this to avoid cycles instead of creating a new node
            dummy.next = node
            dummy = dummy.next
            if temp:
                heappush(min_heap, (temp.val, temp))
        return head.next

    # small edits too
    # space -> O(N) where N is the number of nodes
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        head = dummy = ListNode(0)
        for l in lists:
            while l:  # add all nodes in the heap
                heappush(min_heap, (l.val, l))
                l = l.next

        while min_heap:
            val, node = heappop(min_heap)
            node.next = None
            dummy.next = node
            dummy = dummy.next

        return head.next
