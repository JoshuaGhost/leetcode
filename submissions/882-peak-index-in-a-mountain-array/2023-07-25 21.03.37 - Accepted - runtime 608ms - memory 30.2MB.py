class Solution:
    def rec_mount(self, st, ed):
        if ed - st == 1:
            return st
        if ed - st == 2:
            if self.arr[st] > self.arr[st + 1]:
                return st
            return st + 1
        mid = (ed + st) // 2
        if self.arr[mid] < self.arr[mid + 1]:
            return self.rec_mount(mid + 1, ed)
        return self.rec_mount(st, mid + 1)

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        self.arr = arr
        return self.rec_mount(0, len(arr))