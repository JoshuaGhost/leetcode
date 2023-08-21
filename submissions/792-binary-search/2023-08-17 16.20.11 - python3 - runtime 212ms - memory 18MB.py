class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            ret = self.search(nums[mid + 1:], target)
            if ret == -1:
                return ret
            return mid + 1 + ret
        else:
            return self.search(nums[:mid], target)            