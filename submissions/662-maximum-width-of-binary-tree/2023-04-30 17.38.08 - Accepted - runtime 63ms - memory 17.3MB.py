# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def find_left_most_nodes(node: Optinonal(TreeNode), d:int) -> List[TreeNode]:
    #     res = [(d, node)]
    #     if node.left is not None:
    #         return res + self.find_left_most_nodes(node.left, 0)
    #     elif node.right is not None:
    #         return res + self.find_left_most_nodes(node.right, 1)
    #     return res

    # def find_right_most_nodes(node: Opitonal(TreeNode), d:int) -> List[TreeNode]:
    #     res = [(d, node)]
    #     if node.right is not None:
    #         return res + self.find_right_most_nodes(node.left, 1)
    #     elif node.left is not None:
    #         return res + self.find_right_most_nodes(node.right, 0)
    #     return res

    
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0, 0)]
        p = root
        max_width = 1
        while len(q):
            p, p_addr, level = q[0]
            if level == q[-1][-1]:
                max_width = max(max_width, q[-1][1] - q[0][1] + 1)
            if p.left is not None:
                q.append((p.left, p_addr * 2 + 1, level + 1))
            if p.right is not None:
                q.append((p.right, p_addr * 2 + 2, level + 1))
            q = q[1:]
        return max_width