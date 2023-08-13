class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find_ancestor(p):
            if parent[p] != p:
                parent[p] = find_ancestor(parent[p])
            return parent[p]

        parent = list(range(len(isConnected)))
        for i, neighbour in enumerate(isConnected):
            for j, p in enumerate(neighbour):
                if i == j or p == 0:
                    continue
                parent[find_ancestor(i)] = find_ancestor(j)
        for i in range(len(parent)):
            parent[i] = find_ancestor(i)
        return len(set(parent))