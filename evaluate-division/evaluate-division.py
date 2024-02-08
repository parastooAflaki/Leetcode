class Solution:
    def bfs(self, graph, start, end):


        queue = [(start, 1)]
        visited = defaultdict(int)
        while len(queue) != 0:
            
            queue_first_el = queue.pop(0)
            # print(queue_first_el)
            (node, value) = queue_first_el
            if visited[node] == 1:
                continue
            visited[node] = 1
            if end in graph[node].keys():
                return value * graph[node][end]
            else:
                queue += [(key, value * graph[node][key]) for key in graph[node].keys()]
         
        return -1

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for equation, value in zip(equations, values):
            graph[equation[0]][equation[1]] = value
            graph[equation[1]][equation[0]] = 1 / value

        
        outputs = []
        for query in queries:
            if query[0] not in graph:
                outputs.append(-1)
            else:
                returned_val = self.bfs(graph, query[0], query[1])
                outputs.append(returned_val)

        return outputs
                
        