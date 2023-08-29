# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Tuple


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def _rob(root: Optional[TreeNode]) -> Tuple[int, int]:
            if root is None:
                return 0, 0
            rob_left, skip_left = _rob(root.left)
            rob_right, skip_right = _rob(root.right)
            rob_this = root.val + skip_left + skip_right
            skip_this = max(skip_left, rob_left) + max(skip_right, rob_right)
            return rob_this, skip_this
        return max(*_rob(root))