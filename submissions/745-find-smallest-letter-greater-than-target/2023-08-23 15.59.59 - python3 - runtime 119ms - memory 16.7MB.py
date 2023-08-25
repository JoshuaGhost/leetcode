import bisect

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        p = bisect.bisect(letters, target)
        if p >= len(letters):
            return letters[0]
        return letters[p]