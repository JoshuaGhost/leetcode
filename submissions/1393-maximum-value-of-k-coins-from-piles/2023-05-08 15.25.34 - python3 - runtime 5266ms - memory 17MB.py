from copy import deepcopy


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        ret = [0] * (k + 1)
        prev_ret = [0] * (k + 1)
        coin_total = 0
        for pile in piles:
            coin_total += len(pile)
            cumsum_topk = [0]
            for c in pile[:k]:
                cumsum_topk.append(c + cumsum_topk[-1])
            for i in range(1, min(k + 1, coin_total + 1)):
                for j in range(min(len(pile), k, i), -1, -1):
                    ret[i] = max(prev_ret[i - j] + cumsum_topk[j], ret[i])
            prev_ret = deepcopy(ret)
        return ret[k]
