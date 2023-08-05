class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        if len(questions) == 1:
            return questions[0][0]
        n = len(questions)
        ret = [0] * n
        for idx, (point, brainpower) in zip(range(n - 1, -1, -1), questions[::-1]):
            if idx + brainpower + 1 >= n:
                ret[idx] = max(ret[min(idx + 1, n-1)], point)
            else:
                ret[idx] = max(ret[idx + 1], point + ret[min(n - 1, idx + brainpower + 1)])
        return ret[0]