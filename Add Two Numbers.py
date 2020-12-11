# https://leetcode.com/problems/add-two-numbers/

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time -> O(max(m, n))
# space -> O(max(m, n))
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = head = ListNode(0)
        carry = 0
        while l1 and l2:
            node_sum = l1.val + l2.val + carry
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

        return head.next


# Java Sol
"""
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode p = l1, q = l2, curr = dummyHead;
    int carry = 0;
    while (p != null || q != null) {
        int x = (p != null) ? p.val : 0;
        int y = (q != null) ? q.val : 0;
        int sum = carry + x + y;
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        if (p != null) p = p.next;
        if (q != null) q = q.next;
    }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return dummyHead.next;
}
"""
