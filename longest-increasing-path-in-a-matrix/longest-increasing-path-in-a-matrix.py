class Solution:

    def update_graph_with_given_pos(self, graph, matrix, i_1, j_1, i_2, j_2):
            #make an edge from the smaller to larger node
            if matrix[i_2][j_2] < matrix[i_1][j_1]:
                graph[(i_2, j_2)].add((i_1,j_1))
            elif matrix[i_2][ j_2] > matrix[i_1][j_1]:
                graph[(i_1, j_1)].add((i_2,j_2))


    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        graph = defaultdict(set)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if i - 1 >=0:
                    self.update_graph_with_given_pos(graph, matrix, i, j, i-1, j)
                    
                if i + 1 < len(matrix):
                    #make an edge from the smaller to larger node
                    self.update_graph_with_given_pos(graph, matrix, i, j, i + 1, j)
                
                if j - 1>= 0:
                    self.update_graph_with_given_pos(graph, matrix, i, j, i , j - 1)
                    
                if j + 1 < len(matrix[0]):
                    self.update_graph_with_given_pos(graph, matrix, i, j, i, j + 1)

        if len(matrix) == 1 and len(matrix[0]) == 1:
            return 1

        dp = defaultdict(int)
        for key in graph:
            visited = defaultdict(int)
            queue = [key]

            while len(queue) != 0:
                parent = queue[-1]
                pos_i, pos_j = parent[0], parent[1]
            
                if (pos_i, pos_j) in dp and dp[(pos_i, pos_j)] > 0:
                    queue.pop()
                    continue
                
                elif visited[(pos_i, pos_j)] > 0:
                    children_dps = [1]
                    if parent in graph:
                        for child in graph[parent]:
                            children_dps.append(dp[child] + 1)
                    
                    dp[(pos_i, pos_j)] = max(children_dps)
                    queue.pop()
                    continue
                    
                if parent in graph:
                    queue+= list(graph[parent])

                visited[(pos_i, pos_j)] = 1
       
        return max(dp.values()) 

