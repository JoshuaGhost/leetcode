class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        poses = [False] * (len(s) + 1)
        poses[0] = True
        for ed in range(1, len(s) + 1):
            for st in range(ed - 1, -1, -1):
                if s[st: ed] in wordDict and poses[st]:
                    poses[ed] = True
                    break
        return poses[len(s)]