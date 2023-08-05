class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        nums1, nums2 = zip(*sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True))
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 <= x:
            return 0
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(n):
                dp[j] = max(dp[j], dp[j + 1] + nums2[j] * i + nums1[j])
            for j in range(n - 2, -1, -1):
                dp[j] = max(dp[j + 1], dp[j])
            if sum1 + sum2 * i - max(dp) <= x:
                return i
        return -1