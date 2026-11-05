class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, equation in enumerate(equations):
            a = equation[0]
            b = equation[1]
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))
        

        def bfs(source, target):
            if source not in adj or target not in adj:
                return -1
            visited = set()
            queue = deque([(source, 1)])
            visited.add(source)
            while queue:
                node, w = queue.popleft()
                visited.add(node)
                if node == target:
                    return w
                for nei, weight in adj[node]:
                    if nei in visited:
                        continue
                    queue.append((nei, w * weight))
                    visited.add(nei)
            return -1
        
        result = []
        for q in queries:
            result.append(bfs(q[0], q[1]))
        return result
