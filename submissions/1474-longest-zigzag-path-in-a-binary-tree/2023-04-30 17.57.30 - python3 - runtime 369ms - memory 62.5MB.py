# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_zz_length = 0

    def longest_right_zz(self, n: Optional[TreeNode]) -> int:
        lrz = self.longest_right_zz(n.left) + 1 if n.left is not None else 0
        llz = self.longest_left_zz(n.right) + 1 if n.right is not None else 0
        self.max_zz_length = max(llz, lrz, self.max_zz_length)
        return llz
    
    def longest_left_zz(self, n: Optional[TreeNode]) -> int:
        lrz = self.longest_right_zz(n.left) + 1 if n.left is not None else 0
        llz = self.longest_left_zz(n.right) + 1 if n.right is not None else 0
        self.max_zz_length = max(lrz, llz, self.max_zz_length)
        return lrz

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        llz = self.longest_right_zz(root.left) + 1 if root.left is not None else 0
        lrz = self.longest_left_zz(root.right) + 1 if root.right is not None else 0
        self.max_zz_length = max(llz, lrz, self.max_zz_length)
        return self.max_zz_length