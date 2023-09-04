class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = 1
        while hash(s) != hash(s[::-1]):
            s = ''.join([s[:i - 1], s[-i], s[i - 1:]])
            i += 1
        return s