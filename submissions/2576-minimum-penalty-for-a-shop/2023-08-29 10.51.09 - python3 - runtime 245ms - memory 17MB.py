class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cumsum_y, cumsum_n = 0, 0
        for c in customers:
            cumsum_y += int(c == 'Y')
        least_p, least_p_idx = len(customers) + 1, -1
        customers = ''.join([customers, 'N'])
        for idx, c in enumerate(customers):
            if cumsum_y + cumsum_n < least_p:
                least_p = cumsum_y + cumsum_n
                least_p_idx = idx
            cumsum_y -= int(c == 'Y')
            cumsum_n += int(c == 'N')
        return least_p_idx