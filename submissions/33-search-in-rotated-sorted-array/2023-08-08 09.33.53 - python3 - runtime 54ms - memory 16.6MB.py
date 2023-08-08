class Solution:
    def locate_pivot_spot(self, nums, st, ed):
        if ed - st == 1:
            return st
        if ed - st == 2:
            if nums[st] < nums[ed - 1]:
                return st
            return ed - 1
        if nums[st] < nums[ed - 1]:
            return st
        mid = (st + ed) // 2
        if nums[st] < nums[mid]:
            return self.locate_pivot_spot(nums, mid + 1, ed)
        return self.locate_pivot_spot(nums, st, mid + 1)

    def index_with_rotate(self, target, nums, st, ed):
        if ed == st:
            return -1
        n = len(nums)

        if ed - st == 1:
            if target == nums[st % n]:
                return st % n
            elif target == nums[ed % n]:
                return ed % n
            else:
                return -1
        mid = (ed + st) // 2
        if nums[mid % n] == target:
            return mid % n
        if nums[mid % n] > target:
            return self.index_with_rotate(target, nums, st, mid)
        if nums[mid % n] < target:
            return self.index_with_rotate(target, nums, mid, ed)

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1
        pivot_spot = self.locate_pivot_spot(nums, 0, len(nums))
        return self.index_with_rotate(target, nums, pivot_spot, pivot_spot + len(nums))