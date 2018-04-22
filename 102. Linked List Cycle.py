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
# Hint: Two points, slow one and fast one.
# The fast one will move 2 steps once to catch up with the slow one if there is a cycle.
class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        slow = fast = head
        while slow and fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
            if slow and slow is fast:
                return True
        return False
