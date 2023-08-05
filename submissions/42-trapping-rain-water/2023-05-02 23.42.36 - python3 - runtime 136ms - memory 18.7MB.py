class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = max(height)
        max_height_idx = height.index(max_height)
        s = 0

        highest = 0
        for i in range(max_height_idx):
            s += max(highest - height[i], 0)
            highest = max(highest, height[i])
        
        highest = 0
        for i in range(len(height) - 1, max_height_idx, -1):
            s += max(highest - height[i], 0)
            highest = max(highest, height[i])            

        return s