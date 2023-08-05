class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        t = set()
        for n in nums:
            if n not in t:
                t.add(n)
            else:
                return n