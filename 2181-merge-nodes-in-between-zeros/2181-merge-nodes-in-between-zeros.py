# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode(0)
        head2 = res
        while head:
            count = 0
            while head.val != 0:
                count += head.val
                head = head.next
            res.next = ListNode(0)
            res = res.next
            res.val = count
            head = head.next
            
        return head2.next.next