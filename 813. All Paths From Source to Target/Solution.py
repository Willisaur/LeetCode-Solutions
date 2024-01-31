class Solution:
    def findSolutions(self, i, currentPath, graph, paths):
        # solution
        if len(graph)-1 == i:
            paths.append(currentPath + [len(graph)-1])
            return
        
        # option
        for j in graph[i]:
            self.findSolutions(j, currentPath+[i], graph, paths)

        # nothing worked
        return

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        self.findSolutions(0, [], graph, paths)
        return paths