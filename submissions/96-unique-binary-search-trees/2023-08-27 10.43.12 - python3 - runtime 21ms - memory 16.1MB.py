from typing import Tuple

class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def n_trees(nodes: Tuple[int]) -> int:
            if len(nodes) == 0:
                return 1
            ret = 0
            for i, cur_node in enumerate(nodes):
                ret += n_trees(nodes[: i]) * n_trees(nodes[i + 1:])
            return ret
        if n == 1:
            return n
        return n_trees(tuple(range(n)))