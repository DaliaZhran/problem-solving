# https://leetcode.com/problems/add-two-numbers-ii/

"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(head):
            prev = None
            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            return prev

        l1 = reverseList(l1)
        l2 = reverseList(l2)
        res = head = ListNode(0)
        carry = 0
        while l1 and l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            node_sum = x + y + carry
            carry = node_sum // 10
            res.next = ListNode(node_sum % 10)
            res = res.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            node_sum = l1.val + carry
            carry = node_sum // 10
            res.next = ListNode(node_sum % 10)
            res = res.next
            l1 = l1.next

        while l2:
            node_sum = l2.val + carry
            carry = node_sum // 10
            res.next = ListNode(node_sum % 10)
            res = res.next
            l2 = l2.next

        if carry:
            res.next = ListNode(carry)

        return reverseList(head.next)


# better optimized solution
# Time complexity: O(N1 + N2), N1 + N2 is the number of elements in both lists.
# space: O(1), space complexity without taking the output list into account, and O(max(N1, N2)) to store the output list.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 or l2

        rev_l1 = self.reverseLinkedList(l1)
        rev_l2 = self.reverseLinkedList(l2)
        carry = 0
        res = None
        while rev_l1 or rev_l2:
            n1 = 0 if not rev_l1 else rev_l1.val
            n2 = 0 if not rev_l2 else rev_l2.val

            temp = n1 + n2 + carry
            carry = temp // 10
            curr = ListNode(temp % 10)
            curr.next = res
            res = curr

            rev_l1 = None if rev_l1 == None else rev_l1.next
            rev_l2 = None if rev_l2 == None else rev_l2.next

        if carry:
            curr = ListNode(carry)
            curr.next = res
            res = curr
        return res

    def reverseLinkedList(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


# Follow Up -> No modification for input lists
# use powerful no int limit in python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1, x2 = 0, 0
        while l1:
            x1 = x1 * 10 + l1.val
            l1 = l1.next
        while l2:
            x2 = x2 * 10 + l2.val
            l2 = l2.next
        x = x1 + x2

        head = ListNode(0)
        if x == 0:
            return head
        while x:
            v, x = x % 10, x // 10
            head.next, head.next.next = ListNode(v), head.next

        return head.next


# Using Stack
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = ListNode(0)
        while s1 or s2 or carry:
            if s1:
                carry += s1.pop()
            if s2:
                carry += s2.pop()
            carry, val = divmod(carry, 10)
            head.next, head.next.next = ListNode(val), head.next
        return head.next


# check second solution in question
# https://leetcode.com/problems/add-two-numbers-ii/discuss/687339/Java-O(N)-solution-with-follow-up-question-no-recursion-no-stacks
