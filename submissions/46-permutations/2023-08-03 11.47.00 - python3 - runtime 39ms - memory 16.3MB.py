class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        ret = []
        for idx, n in enumerate(nums):
            for nn in self.permute(nums[:idx] + nums[idx + 1 :]):
                ret.append([n] + nn)
        return ret