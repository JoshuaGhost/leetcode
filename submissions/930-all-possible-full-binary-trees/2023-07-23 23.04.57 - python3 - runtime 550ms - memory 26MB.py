# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [None]
        if n == 1:
            return [TreeNode()]
        else:
            ret = []
            for left_n in range(1, n - 1):
                right_n = n - left_n - 1
                left_trees = self.allPossibleFBT(left_n)
                right_trees = self.allPossibleFBT(right_n)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        ret.append(TreeNode(left=left_tree, right=right_tree))
        return ret