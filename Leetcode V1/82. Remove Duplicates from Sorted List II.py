

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result.next = head

        prev = result
        cur = head

        while cur != None:
            if cur.next and cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next

            cur = cur.next

        return result.next


# public class Solution {
#     public ListNode deleteDuplicates(ListNode head) {
#         if(head == null | |head.next == null) return head

#         if(head.val != head.next.val){
#             head.next = deleteDuplicates(head.next)
#             return head
#         }
#         else{
#             while(head.next != null & &head.val == head.next.val)
#             head = head.next

#             return deleteDuplicates(head.next)
#         }

#     }
# }
