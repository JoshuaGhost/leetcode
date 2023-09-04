class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[-1] > nums[0] or len(nums) == 1:
            return nums[0]
        mid = len(nums) // 2
        if nums[mid] > nums[0]:
            return self.findMin(nums[mid + 1:])
        return self.findMin(nums[1: mid + 1])