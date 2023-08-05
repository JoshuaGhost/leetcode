import bisect

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(enumerate(nums))
        nums = sorted(nums, key=lambda x: x[1])
        print(nums)
        for idx, (i, n) in enumerate(nums):
            j = bisect.bisect_left(nums, target - n, lo=idx+1, key=lambda x: x[1])
            if 0 <= j < len(nums) and n + nums[j][1] == target:
                return [i, nums[j][0]]
