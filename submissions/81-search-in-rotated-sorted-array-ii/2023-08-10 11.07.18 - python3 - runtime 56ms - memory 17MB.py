class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[r - 1]:
                if nums[mid] < target <= nums[r - 1]:
                    l = mid + 1
                else:
                    r = mid
            elif nums[mid] > nums[r - 1]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                r -= 1
        return False
