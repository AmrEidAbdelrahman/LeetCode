# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
            
        for i in range(0, int(round(count/2))):
            head = head.next
            
        return head