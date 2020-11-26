
''' this gives run time error because we loop all the k (think if k is 200000) '''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution(object):
#     def rotateRight(self, head, k):
#         """
#         :type head: ListNode
#         :type k: int
#         :rtype: ListNode
#         """
#         if not head or not k:
#             return head

#         slow, fast = head, head

#         for i in range(k):
#             if fast:
#                 fast = fast.next
#             else:
#                 fast = head.next

#         if not fast:
#             return head

#         while fast and fast.next:
#             fast = fast.next
#             slow = slow.next

#         temp = slow.next
#         slow.next = None
#         fast.next = head

#         return temp


''' This is a better solution -> O(n)'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or not k:
            return head

        fast = head
        length = 1
        while fast.next:
            length += 1
            fast = fast.next
        k = k % length

        slow, fast = head, head
        for i in range(k):
            fast = fast.next

        if not fast or k == 0:
            return head

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        fast.next = head

        return temp
