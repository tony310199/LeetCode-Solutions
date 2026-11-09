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
        dummy = ListNode(0)
        ANS = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                ANS.next = list1
                list1 = list1.next
            else:
                ANS.next = list2
                list2 = list2.next
            ANS = ANS.next
        if list1 == None:
            ANS.next = list2
        elif list2 == None:
            ANS.next = list1
        return dummy.next


        