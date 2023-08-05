class Solution:
    def numberOfSteps(self, num: int) -> int:
        bin_rep = bin(num).__repr__()[3:-1]
        return len(bin_rep) + sum(map(int, bin_rep)) - 1