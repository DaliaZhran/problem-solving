


# my solution

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = head
        while cur != None:
            if  cur.val == prev.val:
                prev.next = cur.next    
            else:
                prev = cur
            cur = cur.next
            
        return head

# better implementation
def deleteDuplicates(self, head):
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head
    