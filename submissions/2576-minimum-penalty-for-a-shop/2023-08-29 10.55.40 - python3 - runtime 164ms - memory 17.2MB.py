class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = 0
        least_p, least_p_idx = 0, 0
        for idx, c in enumerate(customers):
            penalty += int(c == 'N') - int(c == 'Y')
            if penalty < least_p:
                least_p = penalty
                least_p_idx = idx + 1
        return least_p_idx