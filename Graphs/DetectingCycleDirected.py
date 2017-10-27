class Solution(object):
    def __init__(self):
        self.graph = {
                        0: {1, 2},
                        1: {2}
                      }

    def isCyclic(self, p):
        visited = [False] * p
        recStack = [False] * p
        for node in range(p):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        if v in self.graph:
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    if self.isCyclicUtil(neighbor, visited, recStack):
                        return True
                elif recStack[neighbor]:
                    return True
        recStack[v] = False
        return False


print(Solution().isCyclic(3))
