class Solution(object):
    def __init__(self):
        self.graph = {'A': {'B', 'C'},
                      'B': {'A', 'D', 'E'},
                      'C': {'A', 'F'},
                      'D': {'B'},
                      'E': {'B', 'F'},
                      'F': {'C', 'E'}
                      }

    def has_simple_path(self, source, dest):
        stack = [(source, [source])]
        while stack:
            (vertex, path) = stack.pop()
            for nxt in self.graph[vertex] - set(path):
                if nxt == dest:
                    return True
                else:
                    stack.append((nxt, path + [nxt]))
        return False


print(Solution().has_simple_path('A', 'G'))