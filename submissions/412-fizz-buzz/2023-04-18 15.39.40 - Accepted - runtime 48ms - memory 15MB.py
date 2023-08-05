from typing import Union


class Solution:
    @staticmethod
    def _fizz_buzz(n: int) -> str:
        if n % 15 == 0:
            return "FizzBuzz"
        if n % 3 == 0:
            return "Fizz"
        if n % 5 == 0:
            return "Buzz"
        return str(n)

    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            res.append(self._fizz_buzz(i))
        return res