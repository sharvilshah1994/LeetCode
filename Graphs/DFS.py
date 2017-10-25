class Solution(object):
    def __init__(self):
        self.graph = {'A': {'B', 'C'},
                      'B': {'A', 'D', 'E'},
                      'C': {'A', 'F'},
                      'D': {'B'},
                      'E': {'B', 'F'},
                      'F': {'C', 'E'}}

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                stack.extend(self.graph[vertex] - visited)
        return visited


print(Solution().dfs('A'))