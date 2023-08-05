class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        ret = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for idx1, n1 in enumerate(nums1, 1):
            for idx2, n2 in enumerate(nums2, 1):
                if n1 == n2:
                    ret[idx1][idx2] = max(ret[idx1][idx2], ret[idx1 - 1][idx2 - 1] + 1)
                else:
                    ret[idx1][idx2] = max(
                        ret[idx1][idx2],
                        ret[idx1 - 1][idx2],
                        ret[idx1][idx2 - 1],
                        ret[idx1 - 1][idx2 - 1])
        return ret[len(nums1)][len(nums2)]
