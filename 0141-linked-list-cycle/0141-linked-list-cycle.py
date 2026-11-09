# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = head
        slow = head

        ans = False

        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow and fast:
                if slow == fast:
                    return True
            else:
                break
        return ans

        