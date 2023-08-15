# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        p = head
        while True:
            finished = True
            curr = head.next
            prev = head
            pp = None
            while curr:
                if curr.val < x and prev.val >= x:
                    if pp is not None:
                        pp.next = curr
                    prev.next = curr.next
                    curr.next = prev
                    finished = False
                    if prev == head:
                        head = curr
                    pp, prev, curr = pp, curr, prev
                pp, prev, curr = prev, curr, curr.next
            if finished:
                return head