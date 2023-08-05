from collections import deque
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        dq = deque(s[:k])
        count_vowel = 0
        for c in dq:
            if c in vowels:
                count_vowel += 1
        max_count_vowel = count_vowel
        for c in s[k:]:
            dq.append(c)
            c_head = dq.popleft()
            if c_head in vowels:
                count_vowel -= 1
            if c in vowels:
                count_vowel += 1
            max_count_vowel = max(count_vowel, max_count_vowel)

        return max_count_vowel
