class Solution(object):
    def __init__(self):
        self.graph1 = {'A': {'B', 'C'},
                       'B': {'A', 'D', 'E'},
                       'C': {'A', 'F'},
                       'D': {'B'},
                       'E': {'B', 'F'},
                       'F': {'C', 'E'}}

    def detecting_cycle(self, start):
        visited = set()
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex in visited:
                print("Cycle Exists")
                return
            else:
                visited.add(vertex)
                if vertex in self.graph1:
                    stack.extend(self.graph1[vertex] - visited)
        print("Cycle doesn't exist")


Solution().detecting_cycle('A')
