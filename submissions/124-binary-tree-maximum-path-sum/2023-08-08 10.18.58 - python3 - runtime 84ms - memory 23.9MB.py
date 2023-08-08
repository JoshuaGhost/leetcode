# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_sum_ever = -1e1000

    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_sum_as_endpoint = -1e1000
        if root.right is not None:
            right_max_sum = self.max_path_sum(root.right)
        else:
            right_max_sum = -1e1000
        if root.left is not None:
            left_max_sum = self.max_path_sum(root.left)
        else:
            left_max_sum = -1e1000
        max_sum_as_endpoint = max(root.val, root.val + max(right_max_sum, left_max_sum))
        max_sum_no_endpoint = max(
            max_sum_as_endpoint, root.val + right_max_sum + left_max_sum
        )
        self.max_sum_ever = max(
            self.max_sum_ever, max_sum_as_endpoint, max_sum_no_endpoint
        )
        return max_sum_as_endpoint

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum(root)
        return self.max_sum_ever