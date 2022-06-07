# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        print(list1)
        print(list2)
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            res = list1
            list1 = list1.next
        else:
            res = list2
            list2 = list2.next
        res.next = None
        head = res
        print("3", res)    
        while list1 and list2:
            # print(list1.val)
            # list1 = list1.next
            # print(list2.val)
            # list2 = list2.next
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
                res = res.next
            else:
                res.next = list2
                res = res.next
                list2 = list2.next
        while list1:
            res.next = list1
            res = res.next
            list1 = list1.next
        while list2:
            res.next = list2
            res = res.next
            list2 = list2.next
        print(head)
        return head