class Solution(object):
    def __init__(self):
        self.graph = {'A': {'B', 'C'},
                      'B': {'A', 'D', 'E'},
                      'C': {'A', 'F'},
                      'D': {'B'},
                      'E': {'B', 'F'},
                      'F': {'C', 'E'}}

    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.graph[vertex] - visited)
        return visited


print(Solution().bfs('A'))