import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1, nums2 = list(
            zip(
                *sorted(
                    zip(nums1, nums2),
                    key=lambda x: x[1],
                    reverse=True
                )
            )
        )
        current_sum = sum(nums1[:k])
        res = nums2[k - 1] * current_sum
        heap = list(copy.copy(nums1[:k]))
        heapq.heapify(heap)
        p = k
        while p < len(nums1):
            poped = heapq.heappop(heap)
            pushed = nums1[p]
            heapq.heappush(heap, pushed)
            current_sum = current_sum - poped + pushed
            res = max(nums2[p] * current_sum, res)
            p += 1
        return res