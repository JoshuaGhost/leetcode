class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MODULO = int(1e9 + 7)
        sorted_nums = sorted(nums)
        if 2 * sorted_nums[0] > target:
            return 0
        if len(nums) == 1:
            return 1
        l = 0
        r = 1
        res = 1
        max_l = 0
        while r < len(nums):
            if sorted_nums[r] + sorted_nums[0] > target:
                break
            if 2 * sorted_nums[r] <= target:
                res += 1
            if max_l == r - 2:
                max_l = r - 1
            while max_l > 0 and sorted_nums[max_l] + sorted_nums[r] > target:
                max_l -= 1
            l = max_l
            if l == r - 1:
                res += 1
                l -= 1
            if l >= 0:
                res += ((1 << r) - (1 << (r - l - 1))) % MODULO
            # print(r, l, res)
            r += 1
        return res % MODULO
