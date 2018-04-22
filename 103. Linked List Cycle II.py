"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

# Solution 1: Solve the challenge: 
# "Can you solve it without using extra space?"
# 
# Hint: 
# 1. like 102 Linked List Cycle, you can figure out if there is a cycle
# 2. if there is a cycle, move slow point to head, and move both points at the same speed until they meet
#
# Figure:
#   (1)- * - * - * -(2)- * - #
#                    |       |
#                    * - * - *
#
# Assume that they first meet at '#‘, you can prove that 
#        distance(1 -> 2) = distance(# -> 2) + n * length of cycle  (n = 0, 1, 2, ...)
# So if moving distance(1 -> 2) steps, you can return to the origin of the cycle
class Solution:
    """
    @param: head: The first node of linked list.
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        slow = fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow and slow is fast:
                slow = head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
