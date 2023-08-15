class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l_total = len(nums1) + len(nums2)

        def median(a, b, i):
            if not a:
                return b[i]
            if not b:
                return a[i]
            mid_a = len(a) // 2
            mid_b = len(b) // 2
            mid_all = mid_a + mid_b
            if a[mid_a] > b[mid_b]:
                a, b = b, a
                mid_a, mid_b = mid_b, mid_a
            if mid_all < i:
                return median(a[mid_a + 1 :], b, i - mid_a - 1)
            else:
                return median(a, b[:mid_b], i)

        if l_total % 2:
            return median(nums1, nums2, l_total // 2)
        else:
            return (
                median(nums1, nums2, l_total // 2)
                + median(nums1, nums2, l_total // 2 - 1)
            ) / 2
