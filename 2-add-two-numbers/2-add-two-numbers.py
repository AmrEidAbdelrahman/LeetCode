# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res
        remain = 0
        while l1 and l2:
            res.next = ListNode(( l1.val + l2.val + remain ) % 10)
            res = res.next
            remain = ( l1.val + l2.val + remain ) // 10
            l1 = l1.next
            l2 = l2.next
        while l1:
            res.next = ListNode(( l1.val + remain ) % 10)
            res = res.next
            remain = ( l1.val + remain ) // 10
            l1 = l1.next
        while l2:
            res.next = ListNode(( l2.val + remain ) % 10)
            res = res.next
            remain = ( l2.val + remain ) // 10
            l2 = l2.next
        if remain != 0:
            res.next = ListNode(remain)
        return head.next
            
        