class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0
        nums = sorted(nums)
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            i, c = 0, 0
            t, h = 0, 1
            done = False
            while h < len(nums) and c < p:
                if nums[h] - nums[t] <= m:
                    c += 1
                    t += 2
                    h += 2
                else:
                    t += 1
                    h += 1
                if c == p:
                    done = True
                    break
            if done:
                l, r = l, m
            else:
                l, r = m + 1, r
        return l