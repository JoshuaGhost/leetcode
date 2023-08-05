class Solution:
    def half_trap(self, half_height: List[int]) -> int:
        left_highest = half_height[0]
        s = 0
        for i in range(1, len(half_height)):
            if half_height[i] >= left_highest:
                left_highest = half_height[i]
            else:
                s += left_highest - half_height[i]
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