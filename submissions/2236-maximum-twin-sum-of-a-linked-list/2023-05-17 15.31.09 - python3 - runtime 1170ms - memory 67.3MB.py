# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        starting_node = ListNode(next=head)
        node = head
        prev_node = starting_node
        n = 0
        while node is not None:
            node.prev = prev_node
            prev_node = node
            node = node.next
            n += 1

        twin = prev_node
        node = head
        half = n // 2 - 1
        i = 0
        max_sum = 0
        while i <= half:
            max_sum = max(max_sum, node.val + twin.val)
            node = node.next
            twin = twin.prev
            i += 1
        return max_sum
