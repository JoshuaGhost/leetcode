class Solution:
    def index_with_rotate(self, target, nums, st, ed):
        mid = (st + ed) // 2
        if nums[mid] == target:
            return mid
        elif st == ed:
            return -1
        if nums[st] <= nums[mid]:
            if nums[st] <= target <= nums[mid]:
                return self.index_with_rotate(target, nums, st, mid - 1)
            else:
                return self.index_with_rotate(target, nums, mid + 1, ed)
        else:
            if nums[mid] <= target <= nums[ed]:
                return self.index_with_rotate(target, nums, mid + 1, ed)
            else:
                return self.index_with_rotate(target, nums, st, mid - 1)
                
    def search(self, nums: List[int], target: int) -> int:
        return self.index_with_rotate(target, nums, 0, len(nums) - 1)