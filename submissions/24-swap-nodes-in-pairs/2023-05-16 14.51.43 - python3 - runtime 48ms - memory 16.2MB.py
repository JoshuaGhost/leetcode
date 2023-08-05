# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        previous_node = ListNode(next=head)
        starting_node = previous_node
        first_node = None
        while node:
            first_node = node
            node = node.next
            second_node = node
            if node is not None:
                node = node.next
            else:
                previous_node.next = first_node
                break
            previous_node.next = second_node
            second_node.next = first_node
            previous_node = first_node
        if first_node:
            first_node.next = None
        return starting_node.next
