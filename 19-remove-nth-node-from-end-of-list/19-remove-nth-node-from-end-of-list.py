# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = 1
        j = 1
        cup = head
        res = ListNode()
        head2 = res
        while cup.next:
            l += 1
            cup = cup.next
        need_to_delete = l - n + 1
        #print(need_to_delete)
        for i in range(1, l+1):
            # print(head)
            # print(i , need_to_delete)
            if i == need_to_delete:
                head = head.next
            else:
                res.next = ListNode()
                res = res.next
                res.val = head.val
                # print(head2)
                head = head.next
        
        # print(head2.next)
        return head2.next
        
        