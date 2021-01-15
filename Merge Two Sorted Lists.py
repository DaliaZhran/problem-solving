# https://leetcode.com/problems/merge-two-sorted-lists/

# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Approach 1 : Create new heap
# Time : O((N+M)log(M+N))
# Space : O(M + N)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        heap = []
        while l1:
            heappush(heap, l1.val)
            l1 = l1.next
        while l2:
            heappush(heap, l2.val)
            l2 = l2.next

        head = dummy = ListNode(0)

        while heap:
            dummy.next = ListNode(heappop(heap))
            dummy = dummy.next

        return head.next


# Modification
# Time : O(M + N) since max elements in heap is 3 so no cost for pushing and popping
# Space : O(M + N) since we create new nodes
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        heap = []
        head = dummy = ListNode(0)

        while l1 or l2:
            if l1:
                heappush(heap, l1.val)
                l1 = l1.next
            if l2:
                heappush(heap, l2.val)
                l2 = l2.next

            dummy.next = ListNode(heappop(heap))
            dummy = dummy.next

        while heap:
            dummy.next = ListNode(heappop(heap))
            dummy = dummy.next

        return head.next


# Approach 2 : Inplace Merging using pointers
# Time : O(M + N)
# Space : O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = head = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                dummy.next = l2
                l2 = l2.next
            else:
                dummy.next = l1
                l1 = l1.next
            dummy = dummy.next

        dummy.next = l1 if l1 else l2

        return head.next