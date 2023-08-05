from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_vocab = set(ransomNote)
        magazine_vocab = set(magazine)
        if not ransom_vocab.issubset(magazine_vocab):
            return False
        ransom_counter = Counter(ransomNote)
        magazin_counter = Counter(magazine)
        for rc, rn in ransom_counter.items():
            if rn > magazin_counter[rc]:
                return False
        return True