class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)
        while l < r:
            if nums[l] < nums[r - 1]:
                return nums[l]
            elif nums[l] == nums[r - 1]:
                r -= 1
            else:
                mid = (l + r) // 2
                if nums[mid] > nums[l]:
                    l, r = mid + 1, r
                elif nums[mid] < nums[l]:
                    l, r = l + 1, mid + 1
                else:
                    l += 1
        return nums[l]