import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        left = -1 if left == len(nums) or nums[left] != target else left
        if left == -1:
            return -1, -1
        right = bisect.bisect_right(nums, target)
        return [left, right - 1]