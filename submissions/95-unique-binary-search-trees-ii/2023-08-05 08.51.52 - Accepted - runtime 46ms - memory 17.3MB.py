# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def _ones(self, l:int):
        return (1 << l) - 1
    
    def _generate_trees(self, bitmap: int):
        if bitmap in self.dp:
            return self.dp[bitmap]
        ret = []
        for i in range(1, self.n+1):
            if (1 << (i-1)) & bitmap:
                left_trees = self._generate_trees(bitmap & self._ones(i - 1)) if i > 1 else [None]
                right_trees = self._generate_trees(bitmap & (self._ones(self.n) - self._ones(i))) if i < self.n else [None]
                for lt in left_trees:
                    for rt in right_trees:
                        ret.append(TreeNode(i, lt, rt))
        self.dp[bitmap] = ret
        return ret

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        self.n = n
        self.dp = {1<<i: [TreeNode(i + 1)] for i in range(n)}
        self.dp[0] = [None]
        return self._generate_trees((1 << n) - 1)