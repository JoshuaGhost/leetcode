class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            first = max(stones)
            stones.pop(stones.index(first))
            second = max(stones)
            stones.pop(stones.index(second))
            rest = first - second
            if rest != 0:
                stones.append(rest)
        if len(stones) == 0:
            return 0
        return stones[0]