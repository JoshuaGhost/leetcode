class Solution:
    def half_trap(self, half_height: List[int]) -> int:
        left_highest = [0] * len(half_height)
        for i in range(1, len(half_height)):
            if half_height[i] >= half_height[left_highest[i - 1]]:
                left_highest[i] = i
            else:
                left_highest[i] = left_highest[i - 1]
        p = len(half_height) - 1
        s = 0
        while p != 0:
            for h in half_height[left_highest[p - 1] + 1 : p]:
                s += half_height[left_highest[p - 1]] - h
            p = left_highest[p - 1]
        return s
        
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        max_height_idx = height.index(max_height)
        s = 0

        for st in range(max_height_idx):
            if height[st] > height[st + 1]:
                if st != max_height_idx - 1:
                    s += self.half_trap(height[st: max_height_idx + 1])
                break
        
        for ed in range(len(height) - 1, max_height_idx, -1):
            if height[ed] > height[ed - 1]:
                if ed != max_height_idx + 1:
                    s += self.half_trap(height[max_height_idx: ed + 1][::-1])
                break

        return s