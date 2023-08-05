from itertools import chain


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rest = word1[len(word2):] if len(word1) > len(word2) else word2[len(word1):]
        if len(word1) == len(word2):
            rest = ''
        return ''.join(list(chain.from_iterable(zip(word1, word2)))) + rest