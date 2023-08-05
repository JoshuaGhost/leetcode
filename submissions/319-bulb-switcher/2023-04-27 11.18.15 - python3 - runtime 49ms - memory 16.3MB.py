class Solution:
    def bulbSwitch(self, n: int) -> int:
        for i in range(n + 2):
            if i ** 2 > n:
                return i - 1