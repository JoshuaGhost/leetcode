# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        for _ in range(1, k):
            left = left.next
        p_fast = left
        right = head
        while p_fast.next:
            right = right.next
            p_fast = p_fast.next

        right.val, left.val = left.val, right.val
        return head