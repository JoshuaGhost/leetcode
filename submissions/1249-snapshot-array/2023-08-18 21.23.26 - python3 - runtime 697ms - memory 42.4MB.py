import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.mem = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.mem[index][-1][1] == self.snap_id:
            self.mem[index][-1] = (val, self.snap_id)
        else:
            self.mem[index].append((val, self.snap_id))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # print(index, snap_id)
        # print(self.mem[index])
        p = bisect.bisect_left(self.mem[index], snap_id, key=lambda x: x[1])
        # print(p)
        if p == len(self.mem[index]) or (p > 0 and self.mem[index][p - 1][1] <= snap_id and self.mem[index][p][1] != snap_id):
            p -= 1
        # print(p)
        return self.mem[index][p][0]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)