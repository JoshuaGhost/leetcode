class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = 0
        least_p, least_p_idx = len(customers) + 1, -1
        customers = ''.join([customers, 'N'])
        for idx, c in enumerate(customers):
            if penalty < least_p:
                least_p = penalty
                least_p_idx = idx
            penalty += int(c == 'N') - int(c == 'Y')
        return least_p_idx