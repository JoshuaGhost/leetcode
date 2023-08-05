import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        pos = bisect.bisect(self.nums, val)
        if pos == 0 and len(self.nums) == self.k:
            return self.nums[0]
        else:
            self.nums.insert(pos, val)
            self.nums = self.nums[1:] if len(self.nums) > self.k else self.nums
            return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)