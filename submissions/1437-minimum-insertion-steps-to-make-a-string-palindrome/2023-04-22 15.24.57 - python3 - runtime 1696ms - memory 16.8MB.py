class Solution:
    def minInsertions(self, s: str) -> int:
        a = [[1000] * len(s) for _ in range(len(s))]

        for pos in range(len(s)):
            a[pos][pos] = 0
            for p in range(pos + 1, len(s)):
                a[pos][p] = a[pos][p - 1] + 1
            for p in range(pos - 1, -1, -1):
                a[p][pos] = a[p + 1][pos] + 1
        for pos in range(len(s) - 1):
            if s[pos] == s[pos + 1]:
                a[pos][pos + 1] = 0
                for p in range(pos + 2, len(s)):
                    a[pos][p] = a[pos][p - 1] + 1
                for p in range(pos - 1, -1, -1):
                    a[p][pos + 1] = a[p + 1][pos + 1] + 1

        for right_pos, right_char in enumerate(s):
            for left_pos in range(right_pos - 1, -1, -1):
                left_char = s[left_pos]
                a[left_pos][right_pos] = min(
                    a[left_pos][right_pos],
                    a[left_pos][right_pos - 1] + 1)
                if left_pos + 1 < right_pos:
                    a[left_pos][right_pos] = min(
                        a[left_pos][right_pos],
                        a[left_pos + 1][right_pos] + 1,
                        a[left_pos + 1][right_pos - 1] + (0 if left_char == right_char else 2)
                    )
        return a[0][len(s) - 1]