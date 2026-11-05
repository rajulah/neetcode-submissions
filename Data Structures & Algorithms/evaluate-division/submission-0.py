class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for i, equation in enumerate(equations):
            a, b = equation
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        
        def bfs(source, target):
            if source not in adj or target not in adj:
                return -1
            
            queue = deque([(source, 1)])
            visited = set()
            visited.add(source)
            while queue:
                node, w = queue.popleft()
                if node == target:
                    return w
                for neighbor, weight in adj[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, w* weight))
                        visited.add(neighbor)
            return -1
        result = []
        for q in queries:
            result.append(bfs(q[0], q[1]))
        return result







