# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, l: ListNode) -> int:
        p = l
        ret = 0
        while p:
            ret += 1
            p = p.next
        return ret

    def link_sum(self, l1: ListNode, l2: ListNode, pos: int) -> ListNode:
        if l1 is None and l2 is None:
            return 0, None
        ret = ListNode(val = l1.val)
        if pos < self.len_diff:
            add_one, next_node = self.link_sum(l1.next, l2, pos + 1)
            ret.val += add_one
        else:
            add_one, next_node = self.link_sum(l1.next, l2.next, pos + 1)
            ret.val += (add_one + l2.val)
        ret.next = next_node
        
        if ret.val >= 10:
            ret.val -= 10
            return 1, ret
        else:
            return 0, ret           

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len_l1 = self.length(l1)
        len_l2 = self.length(l2)
        if len_l1 < len_l2:
            l1, l2 = l2, l1
            len_l1, len_l2 = len_l2, len_l1
        self.len_diff = len_l1 - len_l2
        add_one, p = self.link_sum(l1, l2, 0)
        if add_one == 1:
            return ListNode(1, p)
        else:
            return p