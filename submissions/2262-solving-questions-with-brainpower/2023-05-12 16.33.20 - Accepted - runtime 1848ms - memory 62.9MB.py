class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        if len(questions) == 1:
            return questions[0][0]
        ret = [0] * len(questions)
        for idx, (point, brainpower) in enumerate(questions):
            ret[idx] = max(ret[idx - 1] if idx != 0 else 0, ret[idx])
            if idx + brainpower + 1 < len(questions):
                ret[idx + brainpower + 1] = max(ret[idx] + point, ret[idx + brainpower + 1])
        return max([r + point for r, (point, _) in zip(ret, questions)])