class Solution(object):
    def __init__(self):
        self.graph = {'A': {'B', 'C'},
                      'B': {'A', 'D', 'E'},
                      'C': {'A', 'F'},
                      'D': {'B'},
                      'E': {'B', 'F'},
                      'F': {'C', 'E'}}

    def get_path_start_end(self, start, end):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for nxt in self.graph[vertex] - set(path):
                if nxt == end:
                    print(path + [nxt])
                else:
                    stack.append((nxt, path + [nxt]))


Solution().get_path_start_end('A', 'B')