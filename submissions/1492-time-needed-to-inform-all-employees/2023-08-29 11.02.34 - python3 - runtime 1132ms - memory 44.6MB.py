from collections import deque, defaultdict


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        fellows = defaultdict(list)
        for emp_id, manager in enumerate(manager):
            fellows[manager].append(emp_id)
        qid = deque([headID])
        qt = deque([0])
        ret = 0
        while qid:
            m, mt = qid.popleft(), qt.popleft()
            for fellow_id in fellows[m]:
                qid.append(fellow_id)
                qt.append(mt + informTime[m])
                ret = max(ret, mt + informTime[m])
        return ret