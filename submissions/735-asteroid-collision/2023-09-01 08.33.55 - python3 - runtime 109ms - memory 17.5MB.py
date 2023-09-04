class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            if not res or res[-1] < 0 or a > 0:
                res.append(a)
            else:
                while res and res[-1] > 0 and abs(a) > abs(res[-1]):
                    res = res[:-1]
                if not res or res[-1] < 0:
                    res.append(a)
                elif abs(a) == abs(res[-1]) and res[-1] > 0:
                    res = res[:-1]
        return res