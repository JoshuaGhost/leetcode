from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        visited = [False] * len(rooms)
        visited[0] = [True]
        while q:
            v = q.popleft()
            for u in rooms[v]:
                if not visited[u]:
                    visited[u] = True
                    q.append(u)
        return all(visited)