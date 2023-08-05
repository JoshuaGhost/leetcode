class Solution:
    mappings = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        d = int(digits[0])
        if len(digits) == 1:
            return list(self.mappings[d])
        ret = []
        for c in self.mappings[d]:
            r = self.letterCombinations(digits[1:])
            for cc in r:
                ret.append(c + cc)
        return ret