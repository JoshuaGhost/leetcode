# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        p = head
        while p.next is not None:
            n = ListNode(self.gcd(p.val, p.next.val))
            n.next = p.next
            p.next = n
            p = n.next
        return head