# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = head
        vals = []
        while p is not None:
            vals.append(p.val)
            p = p.next
        if vals == list(reversed(vals)):
            return True
        return False