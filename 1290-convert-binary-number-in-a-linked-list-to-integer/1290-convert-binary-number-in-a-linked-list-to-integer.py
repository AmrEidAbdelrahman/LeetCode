# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = 0
        base = -1
        temp = head
        while temp:
            base += 1
            temp = temp.next
        while head:
            res += head.val * (2 ** base)
            base -= 1
            head = head.next
        return res
        