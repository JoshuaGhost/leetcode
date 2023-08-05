import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        result = []
        for obstacle in obstacles:
            if not lis or obstacle >= lis[-1]:
                idx = len(lis)
                lis.append(obstacle)
            else:
                idx = bisect.bisect(lis, obstacle)
                lis[idx] = obstacle
            result.append(idx+1)
        return result