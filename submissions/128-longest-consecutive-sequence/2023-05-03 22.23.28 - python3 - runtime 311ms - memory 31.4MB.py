class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        temp = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                num = n
                l = 1
                while num + 1 in nums_set:
                    l += 1
                    num += 1
                longest = max(longest, l)
        return longest