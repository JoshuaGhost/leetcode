from copy import deepcopy
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            "I": 1,
            "X": 10,
            "C": 100,
            "V": 5,
            "L": 50,
            "D": 500,
            "M": 1000
        }
        s_work = deepcopy(s)
        output = 0
        for c in "MDCLXVI":
            pos = [-1]
            for idx, c_current in enumerate(s_work):
                if c_current == c:
                    pos.append(idx)
            if len(pos) == 1:
                continue
            s_process, s_work = s_work[:pos[-1] + 1], s_work[pos[-1] + 1:]
            for start, end in zip(pos[:-1], pos[1:]):
                output += roman_to_int[c]
                for c_minus in s_process[start + 1: end]:
                    output -= roman_to_int[c_minus]
        return output


# if __name__ == '__main__':
#     args = argsparse()
#     solution = Solution