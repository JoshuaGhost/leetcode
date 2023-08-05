class SmallestInfiniteSet:

    def __init__(self):
        self.nums = [1] * 1001
        self.nums[0] = 0

    def popSmallest(self) -> int:
        idx = self.nums.index(1)
        self.nums[idx] = 0
        return idx

    def addBack(self, num: int) -> None:
        self.nums[num] = 1
        return None


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)