class Solution:
    def mul_all(self, l) -> int:
        mul = 1
        for n in l:
            mul *= n
        return mul
    
    def get_first_two_zeros(self, l):
        ret = []
        try:
            idx = l.index(0)
        except ValueError:
            return ret
        ret = [idx]
        try:
            idx = l[ret[0] + 1:].index(0)
        except ValueError:
            return ret
        ret.append(ret[0] + 1 + idx)
        return ret
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        first_two_zeros = self.get_first_two_zeros(nums)
        if len(first_two_zeros) == 2:
            return [0] * len(nums)
        elif len(first_two_zeros) == 1:
            mul = self.mul_all(nums[:first_two_zeros[0]] + nums[first_two_zeros[0] + 1:])
            return [0] * (first_two_zeros[0]) + [mul] + [0] * (len(nums) - first_two_zeros[0] - 1)
        mul = self.mul_all(nums)
        return [mul // n for n in nums]