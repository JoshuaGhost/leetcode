from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        mark = [-1] * len(isConnected)
        for node, neighbours in enumerate(isConnected):
            if mark[node] != -1:
                continue
            mark[node] = node
            visited = [False] * len(isConnected)
            visited[node] = True
            dq = deque([node])
            while dq:
                i = dq.popleft()
                for j, p in enumerate(isConnected[i]):
                    if p == 1 and i != j and not visited[j] and mark[j] == -1:
                        mark[j] = node
                        visited[j] = True
                        dq.append(j)
        return len(set(mark))