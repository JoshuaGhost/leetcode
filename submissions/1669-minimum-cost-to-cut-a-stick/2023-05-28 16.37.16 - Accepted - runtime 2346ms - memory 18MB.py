class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        def _min_cost(l, r, posl, posr, cuts):
            if posr < posl:
                return 0
            if posl == posr:
                min_cost_states[posl][posr] = r - l
                return r - l
            if min_cost_states[posl][posr] is not None:
                return min_cost_states[posl][posr]
            current_min_cost = int(1e15)
            for idx, c in enumerate(cuts):
                if c == 0 or c == n:
                    continue
                cost_left = _min_cost(l, c, posl, posl + idx - 1, cuts[:idx])
                cost_right = _min_cost(c, r, posl + idx + 1, posr, cuts[idx + 1:])
                cost_total = r - l + cost_left + cost_right
                current_min_cost = min(current_min_cost, cost_total)
            min_cost_states[posl][posr] = current_min_cost
            return min_cost_states[posl][posr]
        
        sorted_cuts = sorted(copy.copy(cuts))
        min_cost_states = [[None] * len(cuts) for _ in cuts]
        return _min_cost(0, n, 0, len(cuts) - 1, sorted_cuts)